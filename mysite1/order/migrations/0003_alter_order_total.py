# Generated by Django 3.2.3 on 2021-06-12 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_orderproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=12),
        ),
    ]
