from django.urls import path
from .views import TopUpOrderAPIView, dashboard_view, topup_form_view

urlpatterns = [
    path('', topup_form_view, name='topup-form'),         # Home - HTML form
    path('api/topup/', TopUpOrderAPIView.as_view(), name='topup-api'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
