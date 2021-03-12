from django.contrib.auth.models import User
from django.urls import reverse
from faker import Faker
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APITestCase

from product.models import ProductCategory


class TestProductListCreateAPIViews(APITestCase):

    def setUp(self):
        self.user = baker.make('User')
        self.client.force_authenticate(self.user)
        self.url = reverse('product-list-create')

        self.faker = Faker()

    def test_product_create(self):
        """
        Client requests to create a product!
        :return status code 201 CREATED!
        """


        baker.make('ProductCategory', _quantity=10)
        categories = ProductCategory.objects.all().values_list('id', flat=True)
        requested_data = {
            "name": self.faker.first_name(),
            "default_price": self.faker.random_number(),
            "description": self.faker.first_name(),
            "product_category": list(categories)
        }

        response = self.client.post(self.url, requested_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_list_product(self):
        baker.make('Product', _quantity=10)
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        product_on_list = len(response.json()['results'])

        self.assertGreater(product_on_list, 0)






