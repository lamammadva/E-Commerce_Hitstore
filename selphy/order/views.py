from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Wishlist,Basket

# Create your views here.
def checkout(request):
    return render(request,'checkout.html') 

class BasketView(LoginRequiredMixin,ListView):
    model = Basket
    template_name = 'shopping-cart.html'
    context_object_name = 'basket'
    def get_queryset(self):
        return Basket.objects.filter(user=self.request.user).first()
  
# def shopping_cart(request):
#     return render(request,'shopping-cart.html')

class WishlistView(LoginRequiredMixin, ListView):
    model = Wishlist
    template_name = 'wishlist.html'
    context_object_name = 'wishlist'

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user).first()
