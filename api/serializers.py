import json

from rest_framework import serializers

from api.models import SpendingList


class SpendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpendingList
        fields = ('id', 'description', 'amount', 'spent_at', 'currency')


class NewSpending(serializers.ModelSerializer):
    class Meta:
        model = SpendingList
        fields = ('description', 'amount', 'currency')
