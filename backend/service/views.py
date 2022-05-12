from django.core.serializers.json import DjangoJSONEncoder
from django.http.response import JsonResponse
from datetime import datetime
import backend.databaseHandler.views as database_handler


def get_all_spendings_from_db_handler():
    return JsonResponse(database_handler.get_all_spendings_from_db(), encoder=DjangoJSONEncoder)


def new_spending_to_db_handler(request):
    description = request.POST.get('description')
    amount = request.POST.get('amount')
    spent_at = datetime.date().strftime('%c')
    currency = request.POST.get('currency')

    database_handler.create_new_spending(description, amount, spent_at, currency)


def asc_or_desc(order_type, order):
    if order.equals('ASC'):
        return f'{order_type}'

    if order.equals('DESC'):
        return f'-{order_type}'


def order_spendings_from_db_handler(request):
    order_type = request.GET.get('order_type')
    order = request.GET.get('order')

    if order_type.equals('date'):
        return JsonResponse(database_handler.order_data_by_spendings(asc_or_desc('spent_at', order)),
                            encoder=DjangoJSONEncoder)

    if order_type.equals('amount'):
        return JsonResponse(database_handler.order_data_by_spendings(asc_or_desc('amount', order)),
                            encoder=DjangoJSONEncoder)


def filter_by_currency_from_db_handler(request):
    filter_type = request.GET.get('filter_type')

    if filter_type.equals('ALL'):
        return JsonResponse(database_handler.get_all_spendings_from_db(), encoder=DjangoJSONEncoder)

    return JsonResponse(database_handler.filter_data_by_currency(f'{filter_type}'), encoder=DjangoJSONEncoder)
