from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib import messages

from workshop.forms import WorkshopForm
from workshop.models import Workshop


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