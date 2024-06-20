from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from workshop.models import Workshop


class WorkshopDetailView(LoginRequiredMixin, DetailView):
    model = Workshop
    template_name = 'workshop/workshop_detail.html'
    context_object_name = 'workshop'

    def get_queryset(self):
        return Workshop.objects.filter(owner=self.request.user)