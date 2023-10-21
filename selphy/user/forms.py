from django import forms
from .models import CustomUser

from django.contrib.auth.forms import (
    UserCreationForm, 
    AuthenticationForm, 
    PasswordResetForm,
    SetPasswordForm
    )
class UserRegisterForm(UserCreationForm):

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Your Password'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Your Confirm Password'}))
                                                            
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': "Your First Name"}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': "Your Last Name"}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                            'placeholder': "Your Email Address"}),
        }     
    def clean_password_2(self):
        password1=self.cleaned_data('password1')
        password2=self.cleaned_data('password2')
    


        if password1!=password2:
            raise forms.ValidationError("password and confirm password doesn't match")
        return password2

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control', 
            'placeholder': 'Your Email'
        }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your Password'
        }))

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label="Email Address", widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your Email Address'
        }))
        
class CustomSetPasswordForm(SetPasswordForm):
        new_password1 = forms.CharField(required=True, label='New Password',
            widget=forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your New Password'
                }))
        new_password2 = forms.CharField(required=True, label='Confirm New Password',
            widget=forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Confirm Your New Password'
                }))






















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