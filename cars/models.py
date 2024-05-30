from django.contrib.auth.models import User
from django.db import models

class Car(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    vin = models.CharField(max_length=17, unique=True)
    registration_number = models.CharField(max_length=15)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)


    def __str__(self):
        return f"{self.make} {self.model} ({self.registration_number})"

    class Meta:
        ordering = ['make', 'model', 'year']