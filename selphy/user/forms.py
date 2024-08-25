from django import forms
from .models import CustomUser
from django.contrib.auth.forms import (
    
    UserCreationForm, 
    AuthenticationForm, 
    PasswordResetForm,
    SetPasswordForm
    )
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')
        
class UserLoginForm(AuthenticationForm):
    username = forms.EmailInput()
    password = forms.PasswordInput()

    
   






















# class RegisterForm(forms.ModelForm):
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
#     password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))
#     class Meta:
#         model = CustomUser
#         fields = ['first_name','last_name','email','password1','password2']
#         widgets= {               
#             'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
#             'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'}),
#             'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'name@gmail.com'})

#         }
    
# class LoginForm(forms.Form):
#     email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'your-email@gmail.com'}))
#     password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}))