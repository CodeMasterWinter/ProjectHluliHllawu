# Generated by Django 4.1.3 on 2022-11-17 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hlulihlawu', '0002_orderitem_orders_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='orders_id',
        ),
    ]