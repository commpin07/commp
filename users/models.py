from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media', default='profilepic.jpg')
    description = models.TextField()
    myposts = models.CharField(blank=True,null=True, max_length=300)
    my_bookmarks = models.CharField(blank=True,null=True, max_length=300)
    my_paymentdetails = models.CharField(blank=True,null=True, max_length=300)
    my_wishlist = models.CharField(blank=True,null=True, max_length=300)
    my_scores = models.IntegerField(blank=True,null=True)
    my_itemsview = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.user.username

 
    


