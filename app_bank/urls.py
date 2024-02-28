from rest_framework.routers import DefaultRouter
from .views import CustomerView, AccountView, TransferView, GetTransferView
from django.urls import path, include

app_name = 'bank'

router = DefaultRouter()
router.register('customer', CustomerView, basename='customer')
router.register('account', AccountView, basename='account')
router.register('transfer', TransferView, basename='transfer')

urlpatterns = [
    path('', include(router.urls)),
    path('account/<int:pk>/all_transfers/', GetTransferView.as_view(), name='accounts_transfers'),
]