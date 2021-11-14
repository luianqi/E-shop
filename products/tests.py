from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from products.models import Category, Product, Comment
from users.models import NewUser


class TestProductModels(TestCase):
    def test_models_str(self):
        category = Category.objects.create(name="clothes")
        self.assertEqual(str(category), "clothes")
        supplier = NewUser.objects.create(
            email="supplier@gmail.com", role=1,
            username="supp", password="password"
        )
        client = NewUser.objects.create(
            email="client@gmail.com", role=2,
            username="cli", password="password"
        )
        product = Product.objects.create(
            title="Shirt",
            description="clothes",
            price="50.95",
            discount=50,
            supplier=supplier,
            category=category,
        )
        self.assertEqual(str(product), "Shirt")

        comment = Comment.objects.create(
            product=product, author=client, content="Ew", rate=2
        )
        self.assertEqual(str(comment), "Ew")


class ProductListViewTest(APITestCase):
    def test_get_product_list(self):
        url = reverse("product-list")
        NewUser.objects.create(
            email="supplier@gmail.com", role=1,
            username="sdupp", password="password"
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_product(self):
        url = reverse("product-list")
        user = NewUser.objects.create(
            email="dummy@gmail.com", role=1,
            username="yes", password="password"
        )
        category = Category.objects.create(name="hehehe")
        self.client.force_authenticate(user)
        data = {
            "title": "pop",
            "description": "fantastic skirt",
            "pictures": "lol",
            "price": 42.23,
            "discount": 5,
            "category": category.id,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
