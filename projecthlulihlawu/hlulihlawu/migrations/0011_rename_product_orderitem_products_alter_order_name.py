# Generated by Django 4.1.3 on 2022-11-27 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlulihlawu', '0010_orderitem_open_alter_order_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='product',
            new_name='products',
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(default='<django.db.models.query_utils.DeferredAttribute object at 0x00000205E32940D0> order', max_length=50),
        ),
    ]
