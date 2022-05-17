from django.test import TestCase
from api.models import SpendingList


class TestModels(TestCase):

    def setUp(self):
        spending = SpendingList(description='test', amount=23, currency='HUF')
        spending.save()

    def create_spending(self):
        self.assertEquals(str(self.spending), 'test')

    def get_spending(self):
        query = SpendingList.objects.filter(amount=23)

        self.assertEquals(query, 23)
