from django.urls import path
from .views import checkout,BasketView,WishlistView
urlpatterns = [
    path('checkout/',checkout ,name='checkout'),
    path('shopping_cart/',BasketView.as_view(), name='basket'),
    path('wishlist/',WishlistView.as_view(), name='wishlist')
]