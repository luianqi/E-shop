from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "user",
            "total_price",
            "total_price_with_discount",
            "created_at",
        ]
