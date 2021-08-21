from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Expert(models.Model):
    def __str__(self):
        return self.expert_name

    user_name= models.ForeignKey(User, on_delete=models.CASCADE)
    expert_name = models.CharField(max_length=256, default='name')
    # profile_pic = models.ImageField(upload_to='media', default='profilepic.jpg')
    description = models.CharField(max_length=500)

    


       