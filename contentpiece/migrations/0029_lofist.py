# Generated by Django 2.2 on 2021-08-20 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentpiece', '0028_auto_20210805_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lofist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loi_name', models.CharField(max_length=256)),
            ],
        ),
    ]
