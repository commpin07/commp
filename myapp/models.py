from django.db import models

# Create your models here.

class ItemVid(models.Model):
    # def __str__(self):
    #     return self.item_name

    # item_name = models.CharField(max_length=256, default='video')    
    item_content = models.FileField(upload_to='media')

# review section in app
class Comreview(models.Model):
    def __str__(self):
        return self.comment_article_name

    comment_article_name = models.CharField(max_length=500)
    comment_article = models.TextField(max_length=900)
    

