# cars/models.py
from django.contrib.auth.models import User
from django.db import models

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vin = models.CharField(max_length=17, unique=True)
    registration_number = models.CharField(max_length=10)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    image = models.ImageField(upload_to='car_images', blank=True, null=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.vin})"
