from django.urls import path
from . import views

urlpatterns = [
    path('get-all-spendings/', views.SpendingListView.as_view()),
    path('new-spending', views.NewSpendingView.as_view()),
    path('order-spendings', views.OrderSpendings.as_view()),
    path('filter-by-currency', views.FilterByCurrency.as_view()),
]