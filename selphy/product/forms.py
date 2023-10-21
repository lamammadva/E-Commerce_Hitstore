from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class   Meta:
        model= Review
        fields= ['nickname','comment','quality_rating','price_rating','value_rating'  ]
        widgets={
            'nickname':forms.TextInput(attrs={'placeholder':'Nickname','class':'form-control'}),
            'comment':forms.Textarea(attrs={'placeholder':'Review','class':'form-control'}),
            
        }
