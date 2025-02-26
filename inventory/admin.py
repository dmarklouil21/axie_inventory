from django.contrib import admin
from .models import Axie, Transaction

# Register your models here.

class AxieAdmin(admin.ModelAdmin):
    list_display = ('axie_id', 'breed_count', 'purchase_price', 
                    'purchase_date', 'status') 
    
    ordering = ('axie_id', )

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('axie', 'transaction_type', 'price', 'date')
    
    ordering = ('date', )

admin.site.register(Axie, AxieAdmin)
admin.site.register(Transaction, TransactionAdmin)