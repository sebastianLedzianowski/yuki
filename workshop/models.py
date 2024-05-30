from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, EmailValidator
from PIL import Image

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
phone_validator = RegexValidator(
    regex=r'^\d{9}$',
    message="Numer telefonu musi składać się dokładnie z 9 cyfr.",
    code='invalid_phone'
)

email_validator = EmailValidator(
    message="Podany adres email jest niepoprawny.",
    code='invalid_email'
)


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
    avatar = models.ImageField(default='workshop.png', upload_to='workshop_images')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workshop')

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
