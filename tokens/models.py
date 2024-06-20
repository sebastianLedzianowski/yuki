from django.utils import timezone
from django.db import models

from workshop.models import Workshop


class Subscription(models.Model):
    id = models.BigAutoField(primary_key=True)

    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    workshop = models.OneToOneField(Workshop, on_delete=models.CASCADE, related_name='subscription')

    def __str__(self):
        return f"Subscription for {self.workshop.name}"

    @property
    def is_active(self):
        return self.end_date > timezone.now()


class AccessToken(models.Model):
    id = models.BigAutoField(primary_key=True)

    token = models.CharField(max_length=255, unique=True)
    expiration_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name='tokens')

    def __str__(self):
        return self.token

    @property
    def is_valid(self):
        return self.expiration_date > timezone.now()