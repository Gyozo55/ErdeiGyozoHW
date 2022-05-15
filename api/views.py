from . import service
from rest_framework import generics, status
from .serializers import SpendingSerializer, NewSpending
from .models import SpendingList
from rest_framework.views import APIView
from rest_framework.response import Response


# # First methods
# def get_all_spendings(request):
#     return service.get_all_spendings_from_db_handler()
#
#
# def new_spending(request):
#     return service.new_spending_to_db_handler(request)
#
#
# def order_spendings(request):
#     return service.order_spendings_from_db_handler(request)
#
#
# def filter_by_currency(request):
#     return service.filter_by_currency_from_db_handler(request)
#

# Newone

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
    serializer_class = SpendingSerializer

    def asc_or_desc(self, order_type, order):
        if order == 'ASC':
            return f'{order_type}'

        if order == 'DESC':
            return f'-{order_type}'

    def get(self, request):
        order_type = request.GET.get('order-type')
        order = request.GET.get('order')

        if order_type == 'date':
            # data = SpendingList.objects.order_by(f'{self.asc_or_desc("spent_at", order)}')[0].data
            print(SpendingList.objects.order_by(f'{self.asc_or_desc("spent_at", order)}').values())
            # return Response(SpendingSerializer(data), status=status.HTTP_200_OK)

        if order_type == 'amount':
            # print(SpendingList.objects.order_by(f'{self.asc_or_desc("spent_at", order)}').data)
            return Response(SpendingSerializer(SpendingList.objects.order_by(f'{self.asc_or_desc("amount", order)}'))
                            .data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)


class FilterByCurrency(APIView):
    serializer_class = SpendingSerializer

    def get(self, request):
        filter_type = request.GET.get('filter-type')

        if filter_type == 'ALL':
            return Response(SpendingSerializer(SpendingList.objects.all()), status=status.HTTP_200_OK)
        if filter_type == 'HUF' or filter_type == 'USD':
            return Response(SpendingSerializer(SpendingList.objects.filter(currency=filter_type).all()),
                            status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
