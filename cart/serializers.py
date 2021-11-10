from rest_framework import serializers

from cart.models import CartItem, Cart
from products.serializers import ProductSerializer


class CartItemInputSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()

    class Meta:
        model = CartItem
        fields = ['product_id', 'quantity']


class CartItemOutputSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['product', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    cartitems = CartItemOutputSerializer(many=True, source='cartitem_set')

    class Meta:
        model = Cart
        fields = ['cartitems']


