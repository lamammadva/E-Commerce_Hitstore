from django.urls import path
from .views import ProductApiView
urlpatterns= [
    path('api/product/',ProductApiView.as_view(),name='api_product'),
    # path('api/product/<int:pk>/',ProductApiView.as_view(),name='api_product_detail'),
    path('api/product/<int:pk>/version/<int:version_pk>/',ProductApiView.as_view(),name='api_product_detail'),
   

]