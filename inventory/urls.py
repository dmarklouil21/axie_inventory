from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard_view'),
    path('axie-list/', views.axie_list_view, name='axie_list_view'),
    path('transactions/', views.transaction_list_view, name='transaction_list_view'),
]