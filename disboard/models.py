from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class ItemDib(models.Model):
    def __str__(self):
        return self.item_title

    item_title = models.CharField(max_length=256)
    description = models.CharField(max_length=7000)
    thumbnail = models.ImageField(upload_to='media', default="c.png")  
    name = models.CharField(max_length=256, default=None)
    favs = models.ManyToManyField(User, related_name='favs', default=None, blank=True)

    def get_absolute_url(self):
        return reverse('disboard:detail', kwargs={'pk':self.pk})

class CommentDib(models.Model):
    post = models.ForeignKey(ItemDib, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=256)
    content = models.TextField(max_length=500, default=None)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.post.item_title, str(self.name))        