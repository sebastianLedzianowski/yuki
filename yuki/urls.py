from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('workshop.urls')),
    path('cars/', include('cars.urls')),
    path('repairs/', include('repairs.urls')),
    path('', include('users.urls')),
    path('django-rq/', include('django_rq.urls')),
    path('tokens/', include('tokens.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
