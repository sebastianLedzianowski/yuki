from django.urls import path
from .views.SubscriptionView import SubscriptionView

urlpatterns = [
    path('subscription/<int:pk>/', SubscriptionView.as_view(), name='subscription_detail'),
]
