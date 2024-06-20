from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View

from utils.create_def import create_company


class CEIDGConfirmView(LoginRequiredMixin, View):
    def post(self, request):
        company_data = request.session.get('company_data')

        if company_data:
            return create_company(request, company_data)

        return redirect('workshop_list')