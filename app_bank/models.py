from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Customer(models.Model):
    name = models.CharField(_("Name"), max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Account(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    deposit = models.DecimalField(_("Deposit"), max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = _('Аккаунт клиента')
        verbose_name_plural = _('Аккаунты клиента')

    def __str__(self) -> str:
        return f'Аккаунт id {self.id} пользователя {self.customer.name}'


class Transfer(models.Model):
    sender = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='send_transfer_to')
    recipient = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='receive_transfer_from')
    amount = models.DecimalField(_("Amount"), max_digits=10, decimal_places=2, default=0)
    

    class Meta:
        verbose_name = 'Перевод клиента'
        verbose_name_plural = 'Переводы клиента'

    def __str__(self) -> str:
        return f'''Пользователь {self.sender} (id_acc: {self.sender.id}) перевел на 
    пользователю {self.recipient} (id_acc: {self.recipient.id}) средства в размере {self.amount}'''
