# Generated by Django 3.0.5 on 2024-09-04 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0015_delete_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.CharField(max_length=10),
        ),
    ]
