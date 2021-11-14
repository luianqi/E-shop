from django.db import models
from django.conf import settings

rates = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    pictures = models.CharField(max_length=255, null=False)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    discount = models.IntegerField(default=0)
    supplier = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    content = models.TextField()
    rate = models.IntegerField(choices=rates)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    content = models.TextField()
    rate = models.IntegerField(choices=rates)
    creation_date = models.DateTimeField(auto_now_add=True)
