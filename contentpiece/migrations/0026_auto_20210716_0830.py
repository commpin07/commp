# Generated by Django 2.2 on 2021-07-16 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentpiece', '0025_item_item_viewcount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_viewcount',
            field=models.IntegerField(default=9),
        ),
    ]