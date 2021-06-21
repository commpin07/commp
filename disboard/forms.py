from django import forms
from django.forms import fields

from .models import CommentDib, ItemDib


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentDib

        fields = ['name', 'content']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
        }

class ItemForm(forms.ModelForm):
    class Meta:
        model = ItemDib
        fields = ['item_title', 'description','thumbnail']
        widgets = {
            'item_title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
        }

               