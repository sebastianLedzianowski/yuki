from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from workshop.models import Workshop


class WorkshopListView(LoginRequiredMixin, ListView):
    model = Workshop
    template_name = 'workshop/workshop_list.html'
    context_object_name = 'workshops'

    def get_queryset(self):
        return Workshop.objects.filter(owner=self.request.user)