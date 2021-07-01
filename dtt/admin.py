from django.contrib import admin
from .models import Suggestion, Item, Option, Feedback, YourAnswer

# Register your models here.

admin.site.register(Item)
admin.site.register(Suggestion)
admin.site.register(Option)
admin.site.register(Feedback)
admin.site.register(YourAnswer)
