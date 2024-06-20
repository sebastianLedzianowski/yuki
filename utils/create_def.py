from django.contrib import messages
from django.shortcuts import redirect
from django.utils import timezone
from tokens.models import Subscription, AccessToken
from utils.jwt_tokens import generate_jwt_token
from workshop.models import Workshop


def create_subscription(workshop, days_valid, minutes_valid):
    end_date = timezone.now() + timezone.timedelta(days=days_valid, minutes=minutes_valid)
    subscription = Subscription.objects.create(
        start_date=timezone.now(),
        end_date=end_date,
        workshop=workshop
    )
    return subscription

def create_access_token(subscription, days_valid, minutes_valid):
    expiration_date = timezone.now() + timezone.timedelta(days=days_valid, minutes=minutes_valid)
    token = AccessToken.objects.create(
        token=generate_jwt_token(item_id=subscription.workshop.id, days_valid=days_valid, minutes_valid=minutes_valid),
        expiration_date=expiration_date,
        created_at=timezone.now(),
        subscription=subscription
    )
    return token

def create_company(request, company_data):
    company = Workshop.objects.get_or_create(
        nip=company_data['firmy'][0]['wlasciciel']['nip'],
        defaults={
            'name': company_data['firmy'][0]['nazwa'],
            'regon': company_data['firmy'][0]['wlasciciel']['regon'],
            'address': "{} {}/{}, {} {}".format(
                company_data['firmy'][0]['adresDzialalnosci']['ulica'],
                company_data['firmy'][0]['adresDzialalnosci']['budynek'],
                company_data['firmy'][0]['adresDzialalnosci']['lokal'],
                company_data['firmy'][0]['adresDzialalnosci']['miasto'],
                company_data['firmy'][0]['adresDzialalnosci']['kod'],
            ),
            'create_at': company_data['firmy'][0]['dataRozpoczecia'],
            'owner': request.user
        }
    )
    if company[1]:
        messages.success(request, 'Company added successfully.')
    else:
        messages.info(request, 'Company already exists in the database.')

    return redirect('workshop_list')