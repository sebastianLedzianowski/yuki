from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import WorkshopForm
from .models import Workshop


class WorkshopDeleteView(LoginRequiredMixin, DeleteView):
    model = Workshop
    template_name = 'workshop/workshop_delete.html'
    context_object_name = 'workshop'
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
        messages.error(self.request, 'Correct the following errors:')
        return super().form_invalid(form)


class WorkshopCreateView(LoginRequiredMixin, CreateView):
    model = Workshop
    form_class = WorkshopForm
    template_name = 'workshop/workshop_create.html'
    success_url = reverse_lazy('workshop_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, 'The workshop was created successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Correct the following errors:')
        return super().form_invalid(form)


class WorkshopListView(LoginRequiredMixin, ListView):
    model = Workshop
    template_name = 'workshop/workshop_list.html'
    context_object_name = 'workshops'

    def get_queryset(self):
        return Workshop.objects.filter(owner=self.request.user)


class HomeView(TemplateView):
    template_name = 'index.html'
