from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from order.models import Wishlist, Basket
from .serializers import WishlistSerializer, BasketSerializer
from product.models import Product_version


class WishlistAPIView(APIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    http_method_names = ['get', 'post', 'delete']

    def get(self, request, *args, **kwargs):
        wishlist = Wishlist.objects.filter(user=self.request.user.pk).first()
        serializer = self.serializer_class(wishlist)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        product = request.data.get('product')
        version = Product_version.objects.filter(pk=product).first()
        if version and self.request.user.is_authenticated:
            wishlist = Wishlist.objects.filter(
                user=self.request.user.pk).first()
            if wishlist:
                wishlist.product.add(version)
            else:
                wishlist = Wishlist.objects.create(user=self.request.user)
                wishlist.product.add(version)
            message = {'success': True,
                       'message': 'Product added to your wishlist.'}
            return Response(message, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        product = request.data.get('product')
        version = Product_version.objects.filter(pk=product).first()
        if version and self.request.user.is_authenticated:
            wishlist = Wishlist.objects.filter(user=self.request.user).first()
            if wishlist:
                wishlist.product.remove(version)
                serializer = self.serializer_class(wishlist)

                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class BasketAPIView(APIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    http_method_names = ['get', 'post', 'delete']

    def get(self, request, *args, **kwargs):
        basket = Basket.objects.filter(user=self.request.user).first()
        serializer = self.serializer_class(basket)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        product = request.data.get('product')
        quantity = request.data.get('quantity')
        version = Product_version.objects.filter(pk=product).first()
        if version and self.request.user.is_authenticated:
            basket = Basket.objects.filter(user=self.request.user).first()
            if basket:
                basket_item = basket.items.filter(product=version).first()
                if basket_item:
                    basket_item.quantity += quantity
                    basket_item.save()
                else:
                    basket_item = basket.items.create(
                        user=self.request.user, product=version, quantity=quantity)
            else:
                basket = Basket.objects.create(user=self.request.user)
                basket_item = basket.items.create(
                    user=self.request.user, product=version, quantity=quantity)
            message = {"success": True,
                       "message": "Product added to your basket."}
            return Response(message, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        product = request.data.get('product')
        version = Product_version.objects.filter(pk=product).first()
        if version and self.request.user.is_authenticated:
            basket = Basket.objects.filter(user=self.request.user).first()
            if basket:
                basket_item = basket.items.filter(product=version).first()
                if basket_item:
                    basket_item.delete()
                    message = {"success": True,
                               'message': 'Product removed from your  basket.'}
                    return Response(message, status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
