from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.utils import timezone
from django.views import View

from utils.create_def import create_access_token, create_subscription
from workshop.models import Workshop


class SubscriptionView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        workshop = get_object_or_404(Workshop, pk=kwargs['pk'], owner=request.user)
        subscription = getattr(workshop, 'subscription', None)
        tokens = subscription.tokens.all() if subscription else []

        return render(request, 'tokens/subscription_detail.html', {
            'workshop': workshop,
            'subscription': subscription,
            'tokens': tokens
        })


    def post(self, request, *args, **kwargs):
        workshop = get_object_or_404(Workshop, pk=kwargs['pk'], owner=request.user)
        subscriptions = getattr(workshop, 'subscription', None)

        if subscriptions:
            if subscriptions.is_active:

                messages.info(request, 'The workshop already has an active subscription.')
            else:
                subscriptions.end_date = timezone.now() + timezone.timedelta(days=30)
                subscriptions.save()
                create_access_token(subscriptions, days_valid=30, minutes_valid=0)

                messages.success(request, 'Subscription reactivated successfully.')
        else:
            subscription = create_subscription(workshop, days_valid=30, minutes_valid=0)
            create_access_token(subscription, days_valid=30, minutes_valid=0)

            messages.success(request, 'Subscription purchased successfully.')

        return redirect('subscription_detail', pk=workshop.pk)