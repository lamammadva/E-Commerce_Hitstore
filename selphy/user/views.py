from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import CustomUser
from .forms import UserRegisterForm,UserLoginForm,CustomPasswordResetForm,CustomSetPasswordForm
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
    
def activate(request, uidb64, token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = CustomUser.objects.filter(pk=uid, is_active=False).first()

    if user is not None and account_activation_token.check_token(user, token):
        messages.success(request, 'Your profile is activated')
        user.is_active = True
        user.save()
        return redirect('/login/')
    else:
        messages.error(request, 'Your session is expired')
        return redirect('/')

class RegisterView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super(RegisterView,self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.set_password(form.cleaned_data['password1'])
        form.instance.is_active = False
        form.instance.save()

        subject = 'Activate Your  Account'
        current_site = get_current_site(self.request)
        message = render_to_string('email/confirmation_email.html', {
                'user': form.instance,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(form.instance.pk)),
                'token': account_activation_token.make_token(form.instance),
            })
        from_email = EMAIL_HOST_USER
        to_email = self.request.POST['email']
        send_mail(
            subject,
            message,
            from_email,
            [to_email, ]
        )
        messages.success(self.request, ('Please confirm your email to complete registration.'))
        return redirect('login')

class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'login.html'
    authentication_form = UserLoginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super(CustomLoginView, self).dispatch(request, *args, **kwargs)
    

class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'email/password_message.html'
    form_class = CustomPasswordResetForm
    template_name = 'password/password_reset.html'
    success_url = reverse_lazy('login')
    
    def get_success_url(self):
        messages.success(self.request, 'Your request to change your password has been registered. Please check your email.')
        return super(CustomPasswordResetView, self).get_success_url()   


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password/password_reset_confirm.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('login')

    def get_success_url(self):
        messages.success(self.request, 'Your password has been successfully changed!')
        return super(CustomPasswordResetConfirmView, self).get_success_url()










# class RegisterView(FormView):
#     form_class=RegisterForm
#     template_name='register.html'
#     success_url=reverse_lazy('login')
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

# class LoginView(FormView):
#     form_class=LoginForm
#     template_name='Login.html' 
#     success_url=reverse_lazy('index')
#     def form_valid(self,form):
#         email = form.cleaned_data['email']
#         password = form.cleaned_data['password']
#         user = authenticate(self.request,username=email,password=password)
#         if user:
#             login(self.request, user)
#         return super().form_valid(form)

# Create your views here.
# def register(request):
#     registerform=RegisterForm()
#     if request.method=='POST':
#         registerform=RegisterForm(request.POST)
#         if registerform.is_valid():
#             form=registerform.save(commit=False)
#             form.set_password(registerform.cleaned_data['password1'])
#             form.save()
#             return redirect('login')
#     context={
#         'registerform':registerform 
#     }

#     return render(request,'register.html',context=context)
# def loginform(request):
    
#     if request.method == 'GET':
#         form = LoginForm()
#         return render(request,'login.html', {'form': form})
    
#     elif request.method == 'POST':
#         form = LoginForm(request.POST)
        
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request,username=email,password=password)
#             if user:
#                 login(request, user)
#                 return redirect('/')
#         return render(request,'login.html',{'form': form})

    
    
        
# def sign_out(request):
#     logout(request)
#     # messages.success(request,'You have been logged out.')
#     return redirect('login')        



