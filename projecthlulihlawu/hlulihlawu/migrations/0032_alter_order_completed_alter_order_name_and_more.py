# Generated by Django 4.1.3 on 2022-12-22 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlulihlawu', '0031_remove_order_shipping_model_order_building_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='completed',
            field=models.CharField(choices=[('ordered', 'Awaiting Checkout'), ('checked-out', 'Order Placed'), ('preparing', 'Being Prepared'), ('prepared', 'Completed, awaiting delivery'), ('complete', 'Delivered, Complete')], default='ordered', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(default='<django.db.models.query_utils.DeferredAttribute object at 0x00000186BB41C130> order', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='province',
            field=models.CharField(default='gauteng', max_length=200, null=True),
        ),
    ]
