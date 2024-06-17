from django.urls import path
from .views import WorkshopDeleteView, WorkshopUpdateView, WorkshopListView, HomeView, CEIDGSearchView, CEIDGConfirmView

urlpatterns = [
    path('index/', HomeView.as_view(), name='index'),
    path('workshops/', WorkshopListView.as_view(), name='workshop_list'),
    path('workshop/search/', CEIDGSearchView.as_view(), name='ceidg_search'),
    path('workshop/confirm/', CEIDGConfirmView.as_view(), name='ceidg_confirm'),
    path('workshop/edit/<int:pk>/', WorkshopUpdateView.as_view(), name='workshop_edit'),
    path('workshop/delete/<int:pk>/', WorkshopDeleteView.as_view(), name='workshop_delete')
]