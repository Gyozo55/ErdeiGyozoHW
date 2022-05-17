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

    def get(self, request):
        order_name = request.GET.get('order-name')
        order_type = request.GET.get('order-type')
        if order_name == 'date':
            data = SpendingList.objects.order_by(f'{self.asc_or_desc("spent_at", order_type)}')
            return Response(convert_data_to_valid_json(data), status=status.HTTP_200_OK)

        if order_name == 'amount':
            data = SpendingList.objects.order_by(f'{self.asc_or_desc("amount", order_type)}')
            return Response(convert_data_to_valid_json(data), status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)


def convert_data_to_valid_json(data):
    return convert_data_to_valid_json(data)


class FilterByCurrency(APIView):

    def get(self, request):
        filter_type = request.GET.get('filter-type')

        if filter_type == 'ALL':
            return Response(convert_data_to_valid_json(SpendingList.objects.all()), status=status.HTTP_200_OK)

        if filter_type == 'HUF' or filter_type == 'USD':
            data = SpendingList.objects.filter(currency=filter_type).all()
            return Response(convert_data_to_valid_json(data), status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)


def convert_data_to_valid_json(data):
    serialized_data = json.loads(serializers.serialize('json', data))
    result = []

    for row in serialized_data:
        id = row.get("pk")
        content = row.get("fields")
        content.update({'id': id})
        result.append(content)

    return result


def asc_or_desc(order_name, order_type):
    if order_type == 'ASC':
        return f'{order_name}'

    if order_type == 'DESC':
        return f'-{order_name}'
