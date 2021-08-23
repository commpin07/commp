# Generated by Django 2.2 on 2021-08-23 06:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('langins_name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Price_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ViewMode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Itemblg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=256)),
                ('item_description', models.CharField(max_length=500)),
                ('thumbnail', models.ImageField(default='c.png', upload_to='media')),
                ('item_article', models.FileField(upload_to='media')),
                ('item_viewcount', models.IntegerField(default=1)),
                ('article_viewtype', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.ViewMode')),
                ('favrets', models.ManyToManyField(blank=True, default=None, related_name='favrets', to=settings.AUTH_USER_MODEL)),
                ('loi', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Language')),
                ('user_name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('content', models.TextField(default=None, max_length=500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Itemblg')),
            ],
        ),
    ]
