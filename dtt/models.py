from django.db import models

# Create your models here.
class Option(models.Model):
    def __str__(self):
        return self.option_text

    option_text = models.CharField(max_length=100)

class Feedback(models.Model):
    def __str__(self):
        return self.feedback_text

    feedback_text = models.CharField(max_length=500)    

class YourAnswer(models.Model):
    def __str__(self):
        return self.answer_name

    answer_name = models.CharField(max_length=10)    

class Item(models.Model):
    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=100)
    item_description = models.TextField(max_length=300)
    option1 = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='opt1') 
    option2 = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='opt2')   
    option3 = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='opt3')    
    feedback1 = models.ForeignKey(Feedback, on_delete=models.CASCADE, related_name='fdb1')
    feedback2 = models.ForeignKey(Feedback, on_delete=models.CASCADE, related_name='fdb2')
    feedback3 = models.ForeignKey(Feedback, on_delete=models.CASCADE, related_name='fdb3')
    suggestion = models.CharField(max_length=256, blank=True)
    # answer = models.ForeignKey(YourAnswer, on_delete=models.CASCADE, blank=True, default=1)
    answer = models.CharField(max_length=20, default=1)
    category = models.CharField(max_length=256, blank=True, default=None)
    thumbnail = models.ImageField(upload_to='media', default="c.png")  

class Suggestion(models.Model):
    def __str__(self):
        return self.suggestion_text

    name = models.CharField(max_length=256)
    email = models.EmailField()
    suggestion_text = models.TextField()




    
    
