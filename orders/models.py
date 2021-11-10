from django.db import models
from django.conf import settings


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='owner',
                             on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=50, decimal_places=2)
    total_price_with_discount = models.DecimalField(
        max_digits=50, decimal_places=2
    )




