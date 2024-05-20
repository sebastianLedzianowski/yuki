from django.urls import path
from . import views

urlpatterns = [
    path('', views.workshop_list, name='workshop_list'),
    path('workshop/create', views.workshop_create, name='workshop_create'),
    path('workshop/edit/<int:id>/', views.workshop_edit, name='workshop_edit'),
    path('workshop/delete/<int:id>/', views.workshop_delete, name='workshop_delete')
]