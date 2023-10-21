from django.urls import path
from .views import Blogview,Blogdetailview

urlpatterns = [
    # path('blog/', blog ,name='blog'),
    path('blog/', Blogview.as_view() , name='blog'),

    # path ('blog_details/<int:id>/', blog_details, name='blog_details')
    path('blog_details/<int:pk>/', Blogdetailview.as_view(), name='blog_detail'),
    # path('comment',CommentView.as_view(),name='comment'),

]
