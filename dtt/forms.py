from django import forms
from django.forms import fields

from .models import Item, Suggestion


ANSWER_CHOICES =[

    ('option 1', 'Option 1'),
    ('option 2', 'Option 2'),
    ('option 3', 'Option 3'),
]

class ItemAnswerForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['answer']
        widgets = {
            'answer':forms.Select(choices=ANSWER_CHOICES, attrs={'class':'form-control'}),
            
        }
        
class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['name','suggestion_text']    
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            # 'email':forms.EmailInput(attrs={'class':'form-control'}),
            'suggestion_text':forms.Textarea(attrs={'class':'form-control'}),
        }    