from django.urls import path
from .views import ProductAPIView,ProductVersionAPIView,CategoryAPIView, ColorAPIView
urlpatterns= [
    path('api/product/',CategoryAPIView.as_view(),name='api_product'),
    path('api/version/',ColorAPIView.as_view(),name='version'),
    path('api/products/',ProductAPIView.as_view(),name='api_product_detail'),
    path('api/products/<int:pk>/',ProductAPIView.as_view(),name='api_product_detail'),
    path('api/products/<product_id>/versions/',ProductVersionAPIView.as_view(),name='api_product_version'),
    path('api/products/<product_id>/versions/<int:pk>/',ProductVersionAPIView.as_view(),name='api_product_version')
]