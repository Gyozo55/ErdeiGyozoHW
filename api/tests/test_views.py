from rest_framework.test import APITestCase
from django.urls import reverse


class TestViews(APITestCase):

    def setUp(self):
        self.all_spendings_url = 'allSpendings'
        self.new_spendig_url = 'newSpending'
        self.order_spendings_url = 'orderSpendings'
        self.filter_spendings_url = 'filterSpendings'

    def test_get_all_spendings_GET(self):
        response = self.client.get(reverse(self.all_spendings_url))

        self.assertEquals(response.status_code, 200)

    def test_new_spending_POST(self):
        response = self.client.post(reverse(self.new_spendig_url), {
            'description': 'Iphone',
            'amount': 230000,
            'currency': 'HUF'
        })

        self.assertEquals(response.status_code, 201)

    def test_order_spendings_GET(self):
        response = self.client.get(reverse(self.order_spendings_url), {
            'order-type': '-amount'
        })

        self.assertEquals(response.status_code, 200)

    def test_filter_spendings_GET(self):
        response = self.client.get(reverse(self.filter_spendings_url), {
            'filter-type': 'HUF'
        })

        self.assertEquals(response.status_code, 200)
