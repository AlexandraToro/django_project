# Generated by Django 4.2.3 on 2023-08-05 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side', models.CharField(max_length=10)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
