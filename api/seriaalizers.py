from rest_framework import serializers


class Predictions_currency_Serializers(serializers.Serializer):
    status = serializers.CharField()
    res = serializers.CharField()
