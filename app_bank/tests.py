from rest_framework.test import APITestCase
from .models import Account, Customer
from rest_framework import status
from django.urls import reverse


class CustomerTest(APITestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            name="test_customer"
        )

    def test_create_customer(self):
        data = {"name": self.customer}
        response = self.client.post('/api/customer/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_account_positive(self):
        data = {"customer":self.customer.id, "deposit": 50}
        response = self.client.post('/api/account/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_create_account_string(self):
        data = {"customer":self.customer.id, "deposit": 'string'}
        response = self.client.post('/api/account/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_create_account_negative(self):
        data = {"customer":self.customer.id, "deposit": '-50'}
        response = self.client.post('/api/account/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
class TransferCase(APITestCase):
    
    def setUp(self):
        self.customer1 = Customer.objects.create(name='first_customer')
        self.customer2 = Customer.objects.create(name='second_customer')
        self.account1 = Account.objects.create(customer=self.customer1, deposit=120)
        self.account2 = Account.objects.create(customer=self.customer2, deposit=10)
        
    def test_transfer(self):
        data = {
                    "sender": self.account1.id,
                    "recipient": self.account2.id,
                    "amount": 25
                }
        response = self.client.post('/api/transfer/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.account1.refresh_from_db()
        self.account2.refresh_from_db()
        self.assertEqual(self.account1.deposit, 95)
        self.assertEqual(self.account2.deposit, 35)
        
    def test_transfer_string(self):
        data = {
            "sender": self.account1.id,
            "recipient": self.account2.id,
            "amount": "string"
        }
        response = self.client.post('/api/transfer/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_transfer_id(self):
        data = {
            "sender": 100,
            "recipient": 101,
            "amount": 25
        }
        response = self.client.post('/api/transfer/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_queryset(self):
        url_acc1 = reverse('bank:accounts_transfers', kwargs={'pk': self.account1.pk})
        url_acc2 = reverse('bank:accounts_transfers', kwargs={'pk': self.account2.pk})
        response1 = self.client.get(url_acc1)
        response2 = self.client.get(url_acc2)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)