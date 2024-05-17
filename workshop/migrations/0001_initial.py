# Generated by Django 5.0.6 on 2024-05-17 16:20

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopProfile',
            fields=[
                ('workshop_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('shop_name', models.CharField(blank=True, max_length=100, null=True)),
                ('nip', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_nip', message='NIP musi składać się z 10 cyfr.', regex='^\\d{10}$')])),
                ('regon', models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_regon', message='REGON musi składać się z 9 lub 14 cyfr.', regex='^\\d{9}$|^\\d{14}$')])),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('avatar', models.ImageField(default='workshop.png', upload_to='workshop_images')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workshop', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'workshop',
            },
        ),
        migrations.CreateModel(
            name='AuthorizedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authorized_workshops', to=settings.AUTH_USER_MODEL)),
                ('workshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authorized_users', to='workshop.shopprofile')),
            ],
            options={
                'unique_together': {('user', 'workshop')},
            },
        ),
    ]
