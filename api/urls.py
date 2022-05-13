from django.urls import path
from . import views

urlpatterns = [
    path('get-all-spendings/', views.get_all_spendings),
    path('new-spending/', views.new_spending),
    path('order-spendings/', views.order_spendings),
    path('filter-by-currency/', views.filter_by_currency)
]