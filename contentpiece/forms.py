from django import forms
from django.forms import fields

from .models import Comment, Item

# For new item creation
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_description','thumbnail','article_type','item_article', 'article_viewtype', 'topic', 'language_of_instruction']
       
# to edit existing item
class EditForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_description']


        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'content']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
        }