from rest_framework import serializers

from .models import Taxi, StatusDriver, Order


class TaxiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Taxi
        fields = '__all__'
        read_only_fields = ['profile']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['profile', 'taxi']


class StatusDriverSerializer(serializers.ModelSerializer):

    class Meta:
        model = StatusDriver
        fields = '__all__'
        read_only_fields = ['profile']

