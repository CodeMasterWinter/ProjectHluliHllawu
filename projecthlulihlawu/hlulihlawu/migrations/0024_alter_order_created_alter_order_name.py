# Generated by Django 4.1.3 on 2022-12-19 22:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlulihlawu', '0023_alter_order_created_alter_order_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 19, 22, 37, 0, 843707, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(default='<django.db.models.query_utils.DeferredAttribute object at 0x000001DDAEE90100> order', max_length=100),
        ),
    ]