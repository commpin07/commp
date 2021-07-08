from django.db import models

# Create your models here.

class Item(models.Model):
    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=256)
    item_description = models.CharField(max_length=256)
    item_answer = models.TextField(max_length=500, default="Your answer")
    item_answercount = models.IntegerField(default=1)
    category = models.CharField(max_length=256, blank=True, default="English")
    thumbnail = models.ImageField(upload_to='media', default="c.png")  


class Suggestion(models.Model):
    def __str__(self):
        return self.suggestion_text

    name = models.CharField(max_length=256)
    suggestion_text = models.TextField()