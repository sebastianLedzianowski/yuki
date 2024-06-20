from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from utils.validators import phone_validator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(validators=[phone_validator], max_length=9, null=True, blank=True)
    avatar = models.ImageField(default='avatar.png', upload_to='profile_avatars')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)

            img.save(self.avatar.path)
