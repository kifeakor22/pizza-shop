# Generated by Django 3.0.4 on 2020-04-25 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20200425_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='dinnerplatter',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
    ]
