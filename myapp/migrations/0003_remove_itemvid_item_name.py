# Generated by Django 2.2 on 2021-08-13 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210813_0453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemvid',
            name='item_name',
        ),
    ]
