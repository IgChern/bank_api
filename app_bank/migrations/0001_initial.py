# Generated by Django 4.2.7 on 2024-02-27 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposit', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Deposit')),
            ],
            options={
                'verbose_name': 'Аккаунт клиента',
                'verbose_name_plural': 'Аккаунты клиента',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Amount')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receive_transfer_from', to='app_bank.account')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='send_transfer_to', to='app_bank.account')),
            ],
            options={
                'verbose_name': 'Перевод клиента',
                'verbose_name_plural': 'Переводы клиента',
            },
        ),
        migrations.AddField(
            model_name='account',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_bank.customer'),
        ),
    ]
