from django.urls import path
from .views import  Productview,ProductdetailView
urlpatterns = [
    path('product/',Productview.as_view() ,name='product'),
    path('product_detail/<int:pk>/',ProductdetailView.as_view(),name='product_detail'),
    # path('review/',Review_rate, name='review')
] 