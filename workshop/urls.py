from django.urls import path
from .views.HomeView import HomeView
from .views.WorkshopListView import WorkshopListView
from .views.CEIDGSearchView import CEIDGSearchView
from .views.CEIDGConfirmView import CEIDGConfirmView
from .views.WorkshopDetailView import WorkshopDetailView
from .views.WorkshopUpdateView import WorkshopUpdateView
from .views.WorkshopDeleteView import WorkshopDeleteView

urlpatterns = [
    path('index/', HomeView.as_view(), name='index'),
    path('workshops/', WorkshopListView.as_view(), name='workshop_list'),
    path('workshop/search/', CEIDGSearchView.as_view(), name='ceidg_search'),
    path('workshop/confirm/', CEIDGConfirmView.as_view(), name='ceidg_confirm'),
    path('workshop/<int:pk>/', WorkshopDetailView.as_view(), name='workshop_detail'),
    path('workshop/edit/<int:pk>/', WorkshopUpdateView.as_view(), name='workshop_edit'),
    path('workshop/delete/<int:pk>/', WorkshopDeleteView.as_view(), name='workshop_delete')
]