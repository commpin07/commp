# Generated by Django 2.2 on 2021-07-15 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sean', '0004_auto_20210713_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='tip',
            field=models.CharField(default='Tip', max_length=300),
        ),
    ]
