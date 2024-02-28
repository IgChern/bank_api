from django.apps import AppConfig


class AppBankConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_bank'

    def ready(self):
        import app_bank.signals