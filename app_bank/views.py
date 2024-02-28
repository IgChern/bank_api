from rest_framework.exceptions import ValidationError, NotFound
from .serializers import (AccountSerializer, CustomerSerializer,
                             TransferSerializer)
from .models import Account, Customer, Transfer
from rest_framework.response import Response
from decimal import Decimal
from rest_framework import generics
from rest_framework import viewsets
from django.db import transaction


class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class AccountView(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class TransferView(viewsets.ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer

    def create(self, request, *args, **kwargs):
        sender = request.data['sender']
        recipient = request.data['recipient']
        amount = request.data['amount']
        
        try:
            sender_account = Account.objects.get(pk=sender)
        except Account.DoesNotExist:
            raise NotFound("Аккаунт отправителя не найден")

        try:
            recipient_account = Account.objects.get(pk=recipient)
        except Account.DoesNotExist:
            raise NotFound("Аккаунт получателя не найден")
        
        try:
            amount = float(amount)
        except ValueError:
            raise ValidationError('Сумма перевода должна быть числом')

        if amount > sender_account.deposit:
            raise ValidationError('У отправителя недостаточно средств')
        
        if amount <= 0:
            raise ValidationError('Сумма перевода должна быть положительной')
        
        try:
            amount = Decimal(amount)
            with transaction.atomic():
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                transfer = serializer.save(
                    sender=sender_account,
                    recipient=recipient_account,
                    amount=amount
                )
                sender_account.deposit -= amount
                recipient_account.deposit += amount
                sender_account.save()
                recipient_account.save()

        except Exception as e:
            raise ValidationError(f'Ошибка при выполнении транзакции: {e}')
        
        return Response(TransferSerializer(transfer).data)


class GetTransferView(generics.ListAPIView):
    serializer_class = TransferSerializer

    def get_queryset(self):
        account_id = self.kwargs['pk']
        return Transfer.objects.all().filter(sender__pk=account_id) | Transfer.objects.all().filter(recipient__pk=account_id)