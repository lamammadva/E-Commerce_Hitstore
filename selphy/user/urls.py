from django.urls import path
from .views import RegisterView,LoginView,ForgetPassword,ResetPassword
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view() ,name='register'),
    path('login/', LoginView.as_view() ,name='login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('forget_password/', ForgetPassword.as_view(), name='forget_password'),
    path('reset_password/<str:uidb64>/<str:token>/',ResetPassword.as_view(), name="reset_password"),
]