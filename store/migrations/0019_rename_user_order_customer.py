# Generated by Django 5.0.1 on 2024-01-28 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_order_status_alter_order_address_alter_order_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='customer',
        ),
    ]
