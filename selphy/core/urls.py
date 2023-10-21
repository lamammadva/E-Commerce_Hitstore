from django.urls import path
from .views import About_usView,ContacUsView,faq,IndexView,SearchView

app_name ='goldapp'

urlpatterns = [
    path('about_us/',About_usView.as_view() ,name='about_us'),
    path('contact_us/',ContacUsView.as_view(),name='contact_us'),
    path('faq/',faq,name='faq'),
    path('',IndexView.as_view(),name='index'),
    # path('change_language/',change_language,name='change_language'),
    path('search/',SearchView.as_view(),name='search'),
    # path('change_language/',change_language,name='change_language')
]