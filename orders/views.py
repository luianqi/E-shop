from decimal import Decimal
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import CartItem, Cart
from orders.models import Order
from orders.serializers import OrderSerializer


class OrderView(APIView):
    def post(self, request):

        cart_id = Cart.objects.filter(user=request.user).first()
        print(cart_id)
        cartitems = CartItem.objects.filter(cart=cart_id)
        total_price = 0
        for item in cartitems:
            total_price += item.product.price * item.quantity

        total_price_with_discount = 0
        for item in cartitems:
            discounted_price = (
                Decimal(item.product.price)
                - Decimal((Decimal(item.product.price)
                           * item.product.discount) / 100)) * item.quantity
            total_price_with_discount += discounted_price

        order = Order.objects.create(
            user=request.user,
            total_price=total_price,
            total_price_with_discount=total_price_with_discount
        )

        cartitems.delete()
        cart_id.active = False
        cart_id.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)
