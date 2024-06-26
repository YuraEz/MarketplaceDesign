# Generated by Django 4.2.5 on 2023-09-24 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='final_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='cart',
            name='in_order',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cart',
            name='total_products',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
