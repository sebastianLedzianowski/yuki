from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, EmailValidator
from PIL import Image

nip_validator = RegexValidator(
    regex=r'^\d{10}$',
    message="The NIP must consist of 10 digits.",
    code='invalid_nip'
)
regon_validator = RegexValidator(
    regex=r'^\d{9}$|^\d{14}$',
    message="The REGON must consist of 9 or 14 digits.",
    code='invalid_regon'
)
phone_validator = RegexValidator(
    regex=r'^\d{9}$',
    message="The phone number must consist of exactly 9 digits.",
    code='invalid_phone'
)

email_validator = EmailValidator(
    message="The email address you provided is invalid.",
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
        return self.name if self.name else "No Name"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)
