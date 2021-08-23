from django.contrib import admin
from .models import Itemblg, Language, ViewMode, Comment


# Register your models here.

admin.site.register(Itemblg)
admin.site.register(Language)
admin.site.register(ViewMode)
admin.site.register(Comment)
