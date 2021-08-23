from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse




# Create your models here.


class Language(models.Model):
    def __str__(self):
        return self.langins_name

    langins_name = models.CharField(max_length=256)    



class ViewMode(models.Model):
    def __str__(self):
        return self.genre_name

    genre_name = models.CharField(max_length=100)   

class Price_Category(models.Model):
    def __str__(self):
        return self.price_name

    price_name = models.CharField(max_length=50)     


class Itemblg(models.Model):
    def __str__(self):
        return self.item_name

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=256)
    item_description = models.CharField(max_length=500)
    thumbnail = models.ImageField(upload_to='media', default="c.png")  
    item_article = models.FileField(upload_to='media')
    article_viewtype = models.ForeignKey(ViewMode, on_delete=models.CASCADE,default=None, null=True)
    favrets = models.ManyToManyField(User, related_name='favrets', default=None, blank=True)
    loi = models.ForeignKey(Language, on_delete=models.CASCADE, default=1)
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
#     post = models.ForeignKey(Item, on_delete=models.CASCADE, default=None)
#     value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)    

#     def __str__(self):
#         return str(self.post)     

class Comment(models.Model):
    post = models.ForeignKey(Itemblg, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=256)
    content = models.TextField(max_length=500, default=None)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.post.item_name, str(self.name))


