from .models import SpendingList


def get_all_spendings_from_db():
    return SpendingList.objects.all()


def create_new_spending(description, amount, currency):
    SpendingList(description=description, amount=amount,
                 currency=currency).save()


def order_spendings(order_type):
    return SpendingList.objects.order_by(f'{order_type}')


def filter_data_by_currency(filter_type):
    return SpendingList.objects.filter(currency=filter_type).all()
