# Generated by Django 4.2.3 on 2023-08-05 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice_2', '0002_alter_client_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]