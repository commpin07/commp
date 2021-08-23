from django.contrib import admin
from .models import ItemDib, CommentDib,Language, ViewMode

# Register your models here.

admin.site.register(ItemDib)
admin.site.register(CommentDib)
admin.site.register(Language)
admin.site.register(ViewMode)



