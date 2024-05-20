from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from PIL import Image

class WorkshopProfile(models.Model):
    nip_validator = RegexValidator(
        regex=r'^\d{10}$',
        message="NIP musi składać się z 10 cyfr.",
        code='invalid_nip'
    )
    regon_validator = RegexValidator(
        regex=r'^\d{9}$|^\d{14}$',
        message="REGON musi składać się z 9 lub 14 cyfr.",
        code='invalid_regon'
    )

    objects = models.Manager()

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    nip = models.CharField(validators=[nip_validator], max_length=10, unique=True)
    regon = models.CharField(validators=[regon_validator], max_length=14, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(default='workshop.png', upload_to='workshop_images')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workshop')

    class Meta:
        db_table = "workshop"

    def __str__(self):
        return self.name if self.name else "Brak nazwy"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.avatar.path)

        if img.height > 250 or img.width > 250:
            new_img = (250, 250)
            img.thumbnail(new_img)
            img.save(self.avatar.path)



class AuthorizedUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authorized_workshops')
    workshop = models.ForeignKey(WorkshopProfile, on_delete=models.CASCADE, related_name='authorized_users')


    class Meta:
        unique_together = (('user', 'workshop'),)