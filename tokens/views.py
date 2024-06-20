from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.utils import timezone
from django.views import View

from workshop.models import Workshop
from .models import Subscription, AccessToken
from utils.jwt_tokens import generate_jwt_token


class SubscriptionView(View):
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
        subscription = getattr(workshop, 'subscription', None)

        if subscription:
            if subscription.is_active:
                messages.info(request, 'The workshop already has an active subscription.')
            else:
                subscription.end_date = timezone.now() + timezone.timedelta(days=30)
                subscription.save()
                AccessToken.objects.create(
                    token=generate_jwt_token(workshop.id),
                    expiration_date=timezone.now() + timezone.timedelta(days=30),
                    created_at=timezone.now(),
                    subscription=subscription
                )
                messages.success(request, 'Subscription reactivated successfully.')
        else:
            subscription = Subscription.objects.create(
                start_date=timezone.now(),
                end_date=timezone.now() + timezone.timedelta(days=30),
                workshop=workshop,
            )
            AccessToken.objects.create(
                token=generate_jwt_token(workshop.id),
                expiration_date=timezone.now() + timezone.timedelta(days=30),
                created_at=timezone.now(),
                subscription=subscription,
            )
            messages.success(request, 'Subscription purchased successfully.')

        return redirect('subscription_detail', pk=workshop.pk)
