# Generated by Django 4.1.2 on 2022-10-20 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopcart',
            old_name='p_price',
            new_name='price',
        ),
    ]
