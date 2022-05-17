from django.test import SimpleTestCase
from django.urls import reverse, resolve
from api.views import SpendingListView, NewSpendingView, OrderSpendings, FilterByCurrency


class TestUrls(SimpleTestCase):

    def test_get_all_spendings_is_resolved(self):
        url = reverse('allSpendings')
        self.assertEquals(resolve(url).func.view_class, SpendingListView)

    def test_new_spending_is_resolved(self):
        url = reverse('newSpending')
        self.assertEquals(resolve(url).func.view_class, NewSpendingView)

    def test_order_spendings_is_resolved(self):
        url = reverse('orderSpendings')
        self.assertEquals(resolve(url).func.view_class, OrderSpendings)

    def test_filter_spendings_is_resolved(self):
        url = reverse('filterSpendings')
        self.assertEquals(resolve(url).func.view_class, FilterByCurrency)