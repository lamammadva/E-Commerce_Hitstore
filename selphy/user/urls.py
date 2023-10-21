from django.urls import path
from .views import RegisterView,activate,CustomLoginView,CustomPasswordResetView,CustomPasswordResetConfirmView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view() ,name='register'),
    path('login/', CustomLoginView.as_view() ,name='login'),
    # path('logout/', sign_out, name='logout'),
    path('confirmation/<str:uidb64>/<str:token>/',activate, name='confirmation'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_confirm/<str:uidb64>/<str:token>/',CustomPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
]