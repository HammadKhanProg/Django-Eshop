# Generated by Django 5.0.1 on 2024-01-25 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]
