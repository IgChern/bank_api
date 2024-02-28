from rest_framework import serializers
from .models import Customer, Transfer, Account
from decimal import Decimal
from rest_framework.exceptions import ValidationError


class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = ['id', 'name']

class AccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Account
        fields = ['id', 'customer', 'deposit']
        
    def validate(self, attrs):
        deposit = attrs.get('deposit')
        
        if deposit is None:
            raise ValidationError("Поле 'deposit' не указано")
        
        if deposit < 0:
            raise ValidationError('Депозит должен быть положительным числом')

        if not isinstance(deposit, (int, float, Decimal)):
            raise ValidationError('Депозит должен быть числом')

        return attrs
        
class TransferSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Transfer
        fields = ['id', 'sender', 'recipient', 'amount']

