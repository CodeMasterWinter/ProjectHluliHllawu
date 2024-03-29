# Generated by Django 4.1.3 on 2022-12-22 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlulihlawu', '0038_orderitem_name_alter_order_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(default='<django.db.models.query_utils.DeferredAttribute object at 0x000001CE2C0F4130> order', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='province',
            field=models.CharField(choices=[('gauteng', 'Gauteng'), ('eastern-cape', 'Eastern Cape'), ('free-state', 'Free State'), ('kwaZulu-natal', 'KwaZulu-Natal'), ('limpopo', 'Limpopo'), ('mpumalanga', 'Mpumalanga'), ('northern-cape', 'Northern Cape'), ('north-west', 'North West'), ('western-cape', 'Western Cape')], default='gauteng', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='name',
            field=models.CharField(default='<django.db.models.query_utils.DeferredAttribute object at 0x000001CE2C0F4130>--None', max_length=200),
        ),
    ]
