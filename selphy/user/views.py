from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import CustomUser
from .forms import UserRegisterForm,UserLoginForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.http import urlsafe_base64_decode
# from django.contrib.auth import authenticate, login,logout
from django.views.generic import View,TemplateView,DetailView,ListView,CreateView,UpdateView,DeleteView,FormView
from django.utils.encoding import force_str, force_bytes
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from selphy.settings import EMAIL_HOST_USER
from .tokens import account_activation_token
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetConfirmView, 
    LoginView

)
    

class RegisterView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'
    get_success_url ="login"
    def get_success_url(self):
        return super(RegisterView,self).get_success_url()

    
class LoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'login.html'
    success_url = "index"
    def get_success_url(self):
        return super(LoginView,self).get_success_url()

    

class ForgetPassword(PasswordResetView):
    email_template_name = 'email/password_message.html'
    template_name = 'password/password_reset.html'
    success_url = reverse_lazy('login')
    
    def get_success_url(self):
        messages.success(self.request, 'Your request to change your password has been registered. Please check your email.')
        return super(ForgetPassword, self).get_success_url()   


class ResetPassword(PasswordResetConfirmView):
    template_name = 'password/password_reset_confirm.html'
    success_url = reverse_lazy('login')

    def get_success_url(self):
        messages.success(self.request, 'Your password has been successfully changed!')
        return super(ResetPassword, self).get_success_url()












