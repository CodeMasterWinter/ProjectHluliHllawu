# Generated by Django 4.1.3 on 2022-11-29 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlulihlawu', '0013_remove_orderitem_open_remove_orderitem_products_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size_avail',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(default='<django.db.models.query_utils.DeferredAttribute object at 0x000002581D81C0D0> order', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='flavour',
            field=models.CharField(choices=[('V', 'Vanilla'), ('C', 'Chocolate'), ('U', 'Non-Customizable')], default='V', max_length=100),
        ),
    ]
