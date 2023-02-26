from django.contrib import admin

from .models import Receipt, Debit

# Register your models here.
@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin): 
    list_display = ('name', 'senders', 'money', 'date')

@admin.register(Debit)
class DebitAdmin(admin.ModelAdmin): 
    list_display = ('name', 'name_debit', 'money', 'date', 'status')