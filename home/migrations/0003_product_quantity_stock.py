# Generated by Django 4.2.3 on 2023-07-22 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity_stock',
            field=models.IntegerField(default=0, null=True),
        ),
    ]