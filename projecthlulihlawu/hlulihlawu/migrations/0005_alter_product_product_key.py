# Generated by Django 4.1.3 on 2022-11-18 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlulihlawu', '0004_orderitem_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_key',
            field=models.CharField(choices=[('1126', 'Cakes'), ('1267', 'Cupcakes'), ('2672', 'Cookies'), ('2762', 'Platters')], default='1126', max_length=100),
        ),
    ]
