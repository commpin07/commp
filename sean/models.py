from django.db import models

# Create your models here.

class Item(models.Model):
    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=256)
    item_description = models.CharField(max_length=300)
    item_answer = models.TextField(max_length=700, default="Your answer")
    item_answercount = models.IntegerField(default=1)
    category = models.CharField(max_length=256, blank=True, default="English")
    thumbnail = models.ImageField(upload_to='media', default="c.png")  
    tip = models.CharField(max_length=300, default="Tip")
    appearance = models.CharField(max_length=300, default='appear')


class Suggestion(models.Model):
    def __str__(self):
        return self.suggestion_text

    name = models.CharField(max_length=256)
    suggestion_text = models.TextField()