from django.urls import path
from . import views

urlpatterns = [
    path('', views.repair_list, name='repair_list'),
    path('repair/<int:repair_id>/', views.repair_detail, name='repair_detail'),
    path('repair/add/', views.repair_create, name='repair_create'),
]
