from django.db import models

# Create your models here.

class Item(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=256)
    description = models.CharField(max_length=500)
    
        
