from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import Cart, CartItem
from cart.serializers import CartItemInputSerializer, CartSerializer
from products.models import Product


class CartAdd(APIView):
    def get(self, request):
        cart = Cart.objects.filter(user=request.user).first()
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def post(self, request):
        serializer = CartItemInputSerializer(data=request.data)

        if serializer.is_valid():
            cart = Cart.objects.filter(user=request.user).first()
            product = Product.objects.filter(
                id=serializer.data["product_id"]
            ).first()
            cartitem = CartItem.objects.create(
                product=product,
                quantity=serializer.data["quantity"],
                cart=cart,
            )
            serializer = CartItemInputSerializer(cartitem)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
