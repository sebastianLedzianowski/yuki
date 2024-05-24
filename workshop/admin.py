from django.contrib import admin

from .models import Workshop, AuthorizedUser

admin.site.register(Workshop)
admin.site.register(AuthorizedUser)