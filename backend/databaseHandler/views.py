from backend.databaseHandler.models import SpendingList


def get_all_spendings_from_db():
    return SpendingList.objects.all().value()


def create_new_spending(description, amount, spent_at, currency):
    SpendingList(description=description, amount=amount, spent_at=spent_at,
                 currency=currency).save()


def order_data_by_spendings(order_type):
    return SpendingList.objects.order_by(f'{order_type}')


def filter_data_by_currency(filter_type):
    return SpendingList.objects.filter(curreancy=filter_type).all().value()
