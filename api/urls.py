from django.urls import path
from . import views

urlpatterns = [
    path('get-all-spendings/', views.SpendingListView.as_view(), name='allSpendings'),
    path('new-spending', views.NewSpendingView.as_view(), name='newSpending'),
    path('order-spendings/', views.OrderSpendings.as_view(), name='orderSpendings'),
    path('filter-by-currency/', views.FilterByCurrency.as_view(), name='filterSpendings'),
]