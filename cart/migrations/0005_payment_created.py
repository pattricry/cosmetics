# Generated by Django 4.1.2 on 2022-11-01 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='created',
            field=models.DateField(auto_now=True),
        ),
    ]