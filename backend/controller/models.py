from django.db import models


class SpendingList(models.Model):
    description = models.CharField(max_length=400)
    amount = models.IntegerField()
    spent_at = models.DateField()
    currency = models.CharField(max_length=15)


