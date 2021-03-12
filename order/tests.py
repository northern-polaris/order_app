from django.contrib.auth.models import User

# Create your tests here.
from faker import Faker
from model_bakery import baker
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from order.models import Order


class TestOrderListCreateView(APITestCase):
    def setUp(self):
        self.user = baker.make('User')
        self.client.force_authenticate(self.user)
        self.url = reverse('order-list-create')
        self.faker = Faker()

    def test_order_create(self):
        customer = baker.make('agent.Customer')
        user = User.objects.get(id=1)
        # order = baker.make('order.Order', user=user, customer=customer)

        product1 = baker.make('product.Product')
        product2 = baker.make('product.Product')
        data = {
            'customer_id': customer.id,
            'date_registered': '2021-03-11',
            'order_units':
                [
                    {
                        'product_id': product1.id,
                        'amount': 10,
                        'price': 300,
                    },
                    {
                        'product_id': product2.id,
                        'amount': 10,
                        'price': 200,
                    }
                ],
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, 201)

        order1 = Order.objects.get(id=1)
        order_unit_count = len(order1.order_units.all())
        self.assertEqual(order_unit_count, 2)

        self.assertEqual(order1.customer_id, customer)

    def test_order_list(self):
        baker.make('order.Order', _quantity=12)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

        order_list = response.json()['results']
        self.assertEqual(len(order_list), 10)
