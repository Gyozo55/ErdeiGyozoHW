import json

from django.core import serializers
from rest_framework import generics, status
from .serializers import SpendingSerializer, NewSpending
from .models import SpendingList
from rest_framework.views import APIView
from rest_framework.response import Response


class SpendingListView(generics.ListAPIView):
    queryset = SpendingList.objects.all()
    serializer_class = SpendingSerializer


class NewSpendingView(APIView):
    serializer_class = NewSpending

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            description = serializer.data.get('description')
            amount = serializer.data.get('amount')
            currency = serializer.data.get('currency')

            SpendingList(description=description, amount=amount, currency=currency.upper()).save()

            return Response(status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)


class OrderSpendings(APIView):

    def asc_or_desc(self, order_type, order):
        if order == 'ASC':
            return f'{order_type}'

        if order == 'DESC':
            return f'-{order_type}'

    def get(self, request):
        order_type = request.GET.get('order-type')
        order = request.GET.get('order')
        if order_type == 'date':
            data = SpendingList.objects.order_by(f'{self.asc_or_desc("spent_at", order)}')
            return Response(json.loads(serializers.serialize('json', data)), status=status.HTTP_200_OK)

        if order_type == 'amount':
            data = SpendingList.objects.order_by(f'{self.asc_or_desc("amount", order)}')
            return Response(json.loads(serializers.serialize('json', data)), status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)


class FilterByCurrency(APIView):

    def get(self, request):
        filter_type = request.GET.get('filter-type')

        if filter_type == 'ALL':
            return Response(SpendingSerializer(SpendingList.objects.all()), status=status.HTTP_200_OK)

        if filter_type == 'HUF' or filter_type == 'USD':
            data = SpendingList.objects.filter(currency=filter_type).all()
            return Response(json.loads(serializers.serialize('json', data)), status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
