from django.contrib import admin

from .models import ShopProfile, AuthorizedUser

admin.site.register(ShopProfile)
admin.site.register(AuthorizedUser)