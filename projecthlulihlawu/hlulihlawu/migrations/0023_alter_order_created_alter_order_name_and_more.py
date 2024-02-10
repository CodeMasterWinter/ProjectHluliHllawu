# Generated by Django 4.1.3 on 2022-12-19 22:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlulihlawu', '0022_shippingmodel_building_alter_order_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 19, 22, 36, 34, 847867, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(default='<django.db.models.query_utils.DeferredAttribute object at 0x0000014FA3D6C100> order', max_length=100),
        ),
        migrations.AlterField(
            model_name='shippingmodel',
            name='province',
            field=models.CharField(choices=[('gauteng', 'Gauteng'), ('eastern-cape', 'Eastern Cape'), ('free-state', 'Free State'), ('kwaZulu-natal', 'KwaZulu-Natal'), ('limpopo', 'Limpopo'), ('mpumalanga', 'Mpumalanga'), ('northern-cape', 'Northern Cape'), ('north-west', 'North West'), ('western-cape', 'Western Cape')], default='gauteng', max_length=200),
        ),
    ]