# Generated by Django 3.2.3 on 2021-06-08 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20210608_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=12),
        ),
    ]
