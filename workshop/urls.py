from django.urls import path
from .views import WorkshopDeleteView, WorkshopUpdateView, WorkshopListView, WorkshopCreateView, HomeView


urlpatterns = [
    path('index/', HomeView.as_view(), name='index'),
    path('workshops/', WorkshopListView.as_view(), name='workshop_list'),
    path('workshop/create', WorkshopCreateView.as_view(), name='workshop_create'),
    path('workshop/edit/<int:pk>/', WorkshopUpdateView.as_view(), name='workshop_edit'),
    path('workshop/delete/<int:pk>/', WorkshopDeleteView.as_view(), name='workshop_delete')
]