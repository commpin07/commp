# Generated by Django 2.2 on 2021-06-23 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentpiece', '0021_auto_20210615_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='article_type',
            field=models.CharField(blank=True, default=None, max_length=500),
        ),
    ]
