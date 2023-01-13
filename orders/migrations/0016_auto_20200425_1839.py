# Generated by Django 3.0.4 on 2020-04-25 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_orderitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaOrder',
            fields=[
                ('pizza_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.Pizza')),
                ('quantity', models.IntegerField(default=1)),
            ],
            bases=('orders.pizza',),
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
