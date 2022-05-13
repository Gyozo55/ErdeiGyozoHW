from . import service


def get_all_spendings(request):
    return service.get_all_spendings_from_db_handler()


def new_spending(request):
    return service.new_spending_to_db_handler(request)


def order_spendings(request):
    return service.order_spendings_from_db_handler(request)


def filter_by_currency(request):
    return service.filter_by_currency_from_db_handler(request)
