from django.contrib import admin

from .models import WorkshopProfile, AuthorizedUser

admin.site.register(WorkshopProfile)
admin.site.register(AuthorizedUser)