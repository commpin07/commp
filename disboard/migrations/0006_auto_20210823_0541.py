# Generated by Django 2.2 on 2021-08-23 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disboard', '0005_auto_20210823_0538'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemdib',
            name='article_viewtype',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='disboard.Genre'),
        ),
        migrations.AddField(
            model_name='itemdib',
            name='loi',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='disboard.Langinstr'),
        ),
    ]
