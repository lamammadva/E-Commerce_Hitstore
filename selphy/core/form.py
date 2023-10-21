from django import forms
from .models import Subscriber,ContactUs
from django.forms import widgets

class SubscriberForm(forms.ModelForm):
    class Meta:
        model=Subscriber
        fields=('email',)
        widgets={
            'email':forms.EmailInput(attrs={'class':'form-control validate-email','placeholder':'Enter your email address'})
        }
    def clean_data(self):
        email=self.cleaned_data.get('email')
        if Subscriber.objects.filter(email=email).exists():
            raise forms.ValidationError('email already in use')
        return email
# class SearchForm(forms.Form):
#     name=forms.CharField(required=True)
#     # category_query=forms.CharField(required=True)
class ContacUsForm(forms.ModelForm):
    class Meta:
        model=ContactUs
        fields= ['first_name','last_name','email','message']
        widgets={
            'first_name':forms.TextInput(attrs={'placeholder':'first name','class':'form-control'}),
            'last_name':forms.TextInput(attrs={'placeholder':'last name','class':'form-control'}),
            'email':forms.EmailInput(attrs={'placeholder':'email','class':'form-control'}),
            'message':forms.Textarea(attrs={'placeholder':'message','class':'form-control'}),
            
        }
