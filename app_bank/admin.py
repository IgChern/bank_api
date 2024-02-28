from django.contrib import admin
from .models import Account, Transfer, Customer

# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    search_fields = ('customer', )
    list_display = ('customer', 'deposit')
    
@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    search_fields = ('sender', 'recipient', )
    list_display = ('sender', 'recipient', 'amount', )
    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('name', )