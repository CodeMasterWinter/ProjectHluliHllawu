# Generated by Django 4.1.3 on 2022-12-22 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlulihlawu', '0033_alter_order_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(default='<django.db.models.query_utils.DeferredAttribute object at 0x000002D8757CC160> order', max_length=100),
        ),
    ]
