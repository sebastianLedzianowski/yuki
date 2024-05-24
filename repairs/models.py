# repairs/models.py
from django.db import models
from cars.models import Car
from workshop.models import Workshop

class Repair(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    images = models.ImageField(upload_to='repair_images', blank=True, null=True)
    receipt = models.FileField(upload_to='receipts', blank=True, null=True)
    invoice = models.FileField(upload_to='invoices', blank=True, null=True)

    def __str__(self):
        return f"Repair for {self.car} by {self.workshop}"
