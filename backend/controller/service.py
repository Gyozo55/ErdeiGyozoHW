from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.db.models import QuerySet
from django.http.response import JsonResponse, HttpResponse
from datetime import datetime

from . import databaseHandler
from django.core.serializers import serialize

from django.core.serializers.json import DjangoJSONEncoder


from django.core import serializers


def get_all_spendings_from_db_handler():
    spendings_from_db = databaseHandler.get_all_spendings_from_db()
    print(dir(spendings_from_db))
    return HttpResponse(serializers.serialize('json', spendings_from_db), content_type='application/json')


def new_spending_to_db_handler(request):
    description = request.GET.get('description')
    amount = request.GET.get('amount')
    spent_at = datetime.now()
    currency = request.GET.get('currency')

    databaseHandler.create_new_spending(description, amount, spent_at, currency)


def asc_or_desc(order_type, order):
    if order.equals('ASC'):
        return f'{order_type}'

    if order.equals('DESC'):
        return f'-{order_type}'


def order_spendings_from_db_handler(request):
    order_type = request.GET.get('order_type')
    order = request.GET.get('order')

    if order_type.equals('date'):
        return JsonResponse(databaseHandler.order_data_by_spendings(asc_or_desc('spent_at', order)),
                            encoder=DjangoJSONEncoder)

    if order_type.equals('amount'):
        return JsonResponse(databaseHandler.order_data_by_spendings(asc_or_desc('amount', order)),
                            encoder=DjangoJSONEncoder)


def filter_by_currency_from_db_handler(request):
    filter_type = request.GET.get('filter_type')

    if filter_type.equals('ALL'):
        return JsonResponse(databaseHandler.get_all_spendings_from_db(), encoder=DjangoJSONEncoder)

    return JsonResponse(databaseHandler.filter_data_by_currency(f'{filter_type}'), encoder=DjangoJSONEncoder)
