from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Category, Item, Genre, Like, Comment, Price_Category, Langinstr

# Register your models here.

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


# admin.site.register(MyModelAdmin)
admin.site.register(Category, MyModelAdmin)
admin.site.register(Item)
admin.site.register(Genre)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Price_Category)
admin.site.register(Langinstr)









