# Generated by Django 2.2 on 2021-07-08 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sean', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='thumbnail',
            field=models.ImageField(default='c.png', upload_to='media'),
        ),
    ]
