from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .forms import WorkshopForm, CEIDGSearchForm
from .models import Workshop
import requests
import environ

env = environ.Env(
    DEBUG=(bool, True)
)


class WorkshopDeleteView(LoginRequiredMixin, DeleteView):
    model = Workshop
    success_url = reverse_lazy('workshop_list')

    def get_queryset(self):
        return Workshop.objects.filter(owner=self.request.user)

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'The workshop was deleted successfully.')
        return response


class WorkshopUpdateView(LoginRequiredMixin, UpdateView):
    model = Workshop
    form_class = WorkshopForm
    template_name = 'workshop/workshop_edit.html'
    success_url = reverse_lazy('workshop_list')
    context_object_name = 'workshop'

    def get_queryset(self):
        return Workshop.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, 'The workshop has been successfully updated.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Correct the following errors:')
        return super().form_invalid(form)


class CEIDGSearchView(LoginRequiredMixin, View):
    JWT_TOKEN_CEIDG = env("JWT_TOKEN_CEIDG")
    form_class = CEIDGSearchForm
    template_name = 'workshop/ceidg_search.html'
    success_url = reverse_lazy('workshop_list')

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nip = form.cleaned_data['nip']
            base_url = "https://dane.biznes.gov.pl/api/ceidg/v2/firmy"
            params = {'nip': nip}
            headers = {'Authorization': f'Bearer {self.JWT_TOKEN_CEIDG}'}

            response = requests.get(base_url, params=params, headers=headers)
            if response.status_code == 200:
                data = response.json()
                request.session['company_data'] = data
                return render(request, self.template_name, {'form': form, 'data': data, 'confirm': True})
            else:
                messages.error(request, f"Failed to retrieve data: {response.status_code}")
        else:
            messages.warning(request, "Correct the following errors:")

        return render(request, self.template_name, {'form': form})


class CEIDGConfirmView(LoginRequiredMixin, View):
    def post(self, request):
        company_data = request.session.get('company_data')
        if company_data:
            company, created = Workshop.objects.get_or_create(
                nip=company_data['firmy'][0]['wlasciciel']['nip'],
                defaults={
                    'name': company_data['firmy'][0]['nazwa'],
                    'regon': company_data['firmy'][0]['wlasciciel']['regon'],
                    'address': "{}, {} {}, {}, {}".format(
                        company_data['firmy'][0]['adresDzialalnosci']['ulica'],
                        company_data['firmy'][0]['adresDzialalnosci']['budynek'],
                        company_data['firmy'][0]['adresDzialalnosci']['lokal'],
                        company_data['firmy'][0]['adresDzialalnosci']['miasto'],
                        company_data['firmy'][0]['adresDzialalnosci']['kod'],
                    ),
                    'create_at': company_data['firmy'][0]['dataRozpoczecia'],
                    'owner': self.request.user
                }
            )
            if created:
                messages.success(request, 'Company added successfully.')
            else:
                messages.info(request, 'Company already exists in the database.')

        return redirect('workshop_list')


class WorkshopListView(LoginRequiredMixin, ListView):
    model = Workshop
    template_name = 'workshop/workshop_list.html'
    context_object_name = 'workshops'

    def get_queryset(self):
        return Workshop.objects.filter(owner=self.request.user)


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
