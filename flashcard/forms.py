from django import forms
from django.forms import fields

from .models import CommentFlashCard


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentFlashCard
        fields = ['name', 'content']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
        }