from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.contrib import messages

from workshop.models import Workshop


class WorkshopDeleteView(LoginRequiredMixin, DeleteView):
    model = Workshop
    success_url = reverse_lazy('workshop_list')

    def get_queryset(self):
        return Workshop.objects.filter(owner=self.request.user)

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'The workshop was deleted successfully.')
        return response