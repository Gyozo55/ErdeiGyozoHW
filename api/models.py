from django.db import models


class SpendingList(models.Model):
    description = models.CharField(max_length=400)
    amount = models.IntegerField()
    spent_at = models.DateField(auto_now_add=True)
    currency = models.CharField(max_length=15)

    def __str__(self):
        return self.description

