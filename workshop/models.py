from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from utils.validators import nip_validator, regon_validator, phone_validator, email_validator


class Workshop(models.Model):
    objects = models.Manager()

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    nip = models.CharField(validators=[nip_validator], max_length=10, unique=True)
    regon = models.CharField(validators=[regon_validator], max_length=14, unique=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(validators=[phone_validator], max_length=9, null=True, blank=True)
    email = models.EmailField(validators=[email_validator], max_length=254, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField(null=True, blank=True)
    access_token = models.TextField(null=True, blank=True)
    avatar = models.ImageField(default='workshop.png', upload_to='workshop_images')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workshop')

    class Meta:
        db_table = "workshop"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)
