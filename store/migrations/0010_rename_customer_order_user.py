# Generated by Django 5.0.1 on 2024-01-25 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_customer_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Customer',
            new_name='user',
        ),
    ]
