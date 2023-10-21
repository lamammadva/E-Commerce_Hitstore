from  rest_framework import serializers
from order.models import Wishlist,Basket,Basket_item
from product.api.serializers import ProductversionSerializers



class WishlistSerializer(serializers.ModelSerializer):
    product=ProductversionSerializers(many=True)

    class Meta:
        model = Wishlist
        fields = [
            'user',
            'product',
        ]
class BasketItemSerializer(serializers.ModelSerializer):
    subtotal = serializers.SerializerMethodField()
    product= ProductversionSerializers()
    class Meta:
        model = Basket_item
        fields = [
            'product',
            'quantity',
            'user', 
            'subtotal',
        ]
    def get_subtotal(self,obj):
        return obj.get_subtotal()
    
class BasketSerializer(serializers.ModelSerializer):
    items=BasketItemSerializer(many=True)
    class Meta:
        model = Basket
        fields = [
            'user',
            'items',
        ]
