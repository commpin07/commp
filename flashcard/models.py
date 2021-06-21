from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Genre(models.Model):
    def __str__(self):
        return self.genre_name

    genre_name = models.CharField(max_length=100, default='Image')           

class ItemFC(models.Model):
    def __str__(self):
        return self.item_title

    item_title = models.CharField(max_length=256)
    description = models.CharField(max_length=500)
    thumbnail = models.ImageField(upload_to='media', default="c.png")  
    article = models.ImageField(upload_to='media', null=True, blank=True)  
    article_viewtype = models.ForeignKey(Genre, on_delete=models.CASCADE,default=None, null=True)
    fav = models.ManyToManyField(User, related_name='fav', default=None, blank=True)

    def get_absolute_url(self):
        return reverse('flashcard:detail', kwargs={'pk':self.pk})

class CommentFlashCard(models.Model):
    post = models.ForeignKey(ItemFC, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=256)
    content = models.TextField(max_length=500, default=None)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.post.item_title, str(self.name))

    
        
