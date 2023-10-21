from django.contrib import admin
from .models import Wishlist,Basket,Basket_item
# Register your models here.
# admin.site.register(Order)
admin.site.register(Wishlist)
admin.site.register(Basket)
admin.site.register(Basket_item)