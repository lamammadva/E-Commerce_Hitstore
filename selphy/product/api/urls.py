from django.urls import path
from .views import ProductApiView,ProductVersionApiView
urlpatterns= [
    path('api/product/',ProductApiView.as_view(),name='api_product'),
    path('api/product/<int:pk>/',ProductApiView.as_view(),name='api_product_detail'),
    path('api/product_version/',ProductVersionApiView.as_view(),name='api_product_version'),
    

#     path('api/products/<product_id>/versions/',ProductVersionAPIView.as_view(),name='api_product_version'),
#     path('api/products/<product_id>/versions/<int:pk>/',ProductVersionAPIView.as_view(),name='api_product_version')
]