# Generated by Django 4.1.3 on 2022-11-26 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlulihlawu', '0006_product_flavour_avail'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default='<django.db.models.query_utils.DeferredAttribute object at 0x000002C5757B0250> order', max_length=50),
        ),
    ]