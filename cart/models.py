from django.conf import settings
from django.db import models

from products.models import Product


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)


class CartItem(models.Model):
    product = models.ForeignKey(Product, related_name='cart_item', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, null=True, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)



