from django.db import models
from selphy.utils.base import BaseModel
from user.models import CustomUser
from product.models import Product_version
# Create your models here.

class Wishlist(BaseModel):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name='wishlist_name')
    product = models.ManyToManyField(
        Product_version, related_name='product_name')

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'


class Basket_item(BaseModel):
    product = models.ForeignKey(
        Product_version, on_delete=models.CASCADE, related_name='basket_product')
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='basket_user')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.email}'s  basket item"
    

    def get_subtotal(self):
        if self.product.product.sale:
          return self.product.product.old_price * self.quantity
        else:
          return self.product.product.price * self.quantity


    
    class Meta:
        verbose_name = 'Basket Item '
        verbose_name_plural = 'Baskets Items'


class Basket(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(Basket_item, related_name='basket_items')

    def __str__(self):
        return f"{self.user.email}'s basket"

    class Meta:
        verbose_name = 'Basket'
        verbose_name_plural = 'Baskets'
