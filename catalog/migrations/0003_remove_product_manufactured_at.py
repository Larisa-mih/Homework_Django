# Generated by Django 5.0.3 on 2024-03-31 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_product_manufactured_at_alter_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='manufactured_at',
        ),
    ]