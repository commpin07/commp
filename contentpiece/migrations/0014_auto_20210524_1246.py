# Generated by Django 2.2 on 2021-05-24 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contentpiece', '0013_auto_20210524_1245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='user',
        ),
    ]
