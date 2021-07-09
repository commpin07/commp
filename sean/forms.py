from django import forms
from django.forms import fields

from .models import Item, Suggestion



class ItemAnswerForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_answer']
        widgets = {
            'item_answer':forms.Textarea(attrs={'class':'form-control'}),
            
        }     
        
class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['name','suggestion_text']    
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'suggestion_text':forms.Textarea(attrs={'class':'form-control'}),
        }            