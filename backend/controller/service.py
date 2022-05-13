import json
from django.http.response import JsonResponse
from datetime import datetime
from . import databaseHandler
from django.core import serializers


# Convert to Json
def convert_data_to_valid_json(data):
    serialized_data = json.loads(serializers.serialize('json', data))
    dict_response = {}

    for row in serialized_data:
        id = row.get("pk")
        content = row.get("fields")
        dict_response.update({id: content})

    return dict_response


# All Spending
def get_all_spendings_from_db_handler():
    spendings_from_db = databaseHandler.get_all_spendings_from_db()
    json_data = convert_data_to_valid_json(spendings_from_db)
    return JsonResponse(json_data)


# New Spending
def new_spending_to_db_handler(request):
    description = request.GET.get('description')
    amount = request.GET.get('amount')
    spent_at = datetime.now()
    currency = request.GET.get('currency')

    databaseHandler.create_new_spending(description, amount, spent_at, currency)


# Order
def asc_or_desc(order_type, order):
    if order == 'ASC':
        return f'{order_type}'

    if order == 'DESC':
        return f'-{order_type}'


def order_spendings_from_db_handler(request):
    order_type = request.GET.get('order-type')
    order = request.GET.get('order')

    if order_type == 'date':
        order_data_by_date = databaseHandler.order_spendings(asc_or_desc('spent_at', order))
        json_data = convert_data_to_valid_json(order_data_by_date)
        return JsonResponse(json_data)

    if order_type == 'amount':
        order_data_by_amount = databaseHandler.order_spendings(asc_or_desc('amount', order))
        json_data = convert_data_to_valid_json(order_data_by_amount)
        return JsonResponse(json_data)


# Filter
def filter_by_currency_from_db_handler(request):
    filter_type = request.GET.get('filter-type')

    if filter_type == 'ALL':
        from_db = databaseHandler.get_all_spendings_from_db()
        json_data = convert_data_to_valid_json(from_db)
        return JsonResponse(json_data)

    filter_data_by_currency = databaseHandler.filter_data_by_currency(f'{filter_type}')
    json_data = convert_data_to_valid_json(filter_data_by_currency)
    return JsonResponse(json_data)
