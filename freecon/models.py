from django.db import models
from django.db.models.fields import CharField
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User
from django.urls import reverse




# Create your models here.
class Category(models.Model):
    def __str__(self):
        return self.category_name

    category_name = models.CharField(max_length=256)


class Genre(models.Model):
    def __str__(self):
        return self.genre_name

    genre_name = models.CharField(max_length=100)   

class Price_Category(models.Model):
    def __str__(self):
        return self.price_name

    price_name = models.CharField(max_length=50)           

class Itemfreecon(models.Model):
    def __str__(self):
        return self.item_name

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=256)
    item_description = models.CharField(max_length=500)
    thumbnail = models.ImageField(upload_to='media', default="c.png")  
    # articlelink = EmbedVideoField(default='https://www.youtube.com/watch?v=J3MuH6xaDjI&t=493s', blank=True)
    item_article = models.FileField(upload_to='media')
    article_type = models.CharField(max_length=500, default=None, blank=True)
    topic = models.ForeignKey(Category, on_delete=models.CASCADE,default=None)
    article_viewtype = models.ForeignKey(Genre, on_delete=models.CASCADE,default=None, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    # likd = models.ManyToManyField(User, related_name='likd', default=None, blank=True)
    favre = models.ManyToManyField(User, related_name='favre', default=None, blank=True)
    language_of_instruction = models.CharField(max_length=100, default="English")
    item_pricecategory = models.ForeignKey(Price_Category, on_delete=models.CASCADE, default=1)
    item_viewcount = models.IntegerField(default=1)
    
 
    
    def get_absolute_url(self):
        return reverse('contentpiece:detail', kwargs={'pk':self.pk})

    @property
    def num_likes(self):
        return self.liked.all().count()

# LIKE_CHOICES = (
#     ('Like', 'Like'),
#     ('Unlike', 'Unlike'),
# )

# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
#     post = models.ForeignKey(Itemfreecon, on_delete=models.CASCADE, default=None)
#     value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)    

#     def __str__(self):
#         return str(self.post)     

class Comment(models.Model):
    post = models.ForeignKey(Itemfreecon, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=256)
    content = models.TextField(max_length=500, default=None)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.post.item_name, str(self.name))




    