from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages

from workshop.forms import CEIDGSearchForm
from yuki.settings import env
import requests


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