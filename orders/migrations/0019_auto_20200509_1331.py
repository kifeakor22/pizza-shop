# Generated by Django 3.0.4 on 2020-05-09 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_auto_20200509_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pizza_style',
            field=models.CharField(blank=True, choices=[('Regular pizza', 'Regular pizza'), ('Sicilian pizza', 'Sicilian pizza')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, choices=[('small', 'small'), ('large', 'large')], max_length=10, null=True),
        ),
    ]