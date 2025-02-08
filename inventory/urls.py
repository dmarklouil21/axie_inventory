from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard_view'),
    path('axies/', views.axie_list_view, name='axies_view'),
    path('axies/add-axie/', views.add_axie_form_view, name='add_axie_view'),
    path('axies/edit-axie/<int:axie_id>/', views.edit_axie_form_view, name='edit_axie_form_view'),
    path('transactions/', views.transaction_list_view, name='transaction_list_view'),
]