# Generated by Django 5.0.1 on 2024-02-02 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_alter_product_item_code'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('item_code', 'id')},
        ),
    ]