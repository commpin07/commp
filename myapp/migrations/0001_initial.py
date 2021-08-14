# Generated by Django 2.2 on 2021-08-13 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(default='video', max_length=256)),
                ('item_content', models.FileField(upload_to='media')),
            ],
        ),
    ]