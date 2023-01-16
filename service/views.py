from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response

from service.models import Taxi, Order, StatusDriver
from service.permissions import IsDriverOrReadOnly, IsOwnerOrReadOnly, IsClientOrReadOnly, IsAuthenticated
from service.serializers import TaxiSerializer, OrderSerializer, StatusDriverSerializer


class TaxiViewSet(viewsets.ModelViewSet):
    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer
    permission_classes = [IsDriverOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)


class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(taxi_id=self.kwargs.get('taxi_id'))

    def perform_create(self, serializer):
        serializer.save(
            profile=self.request.user.profile,
            taxi_id=self.kwargs.get('taxi_id')
        )


class OrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(taxi_id=self.kwargs.get('taxi_id'))

    def perform_create(self, serializer):
        serializer.save(
            profile=self.request.user.profile,
            taxi_id=self.kwargs.get('taxi_id')
        )


class StatusDriverViewSet(viewsets.ModelViewSet):
    queryset = StatusDriver.objects.all()
    serializer_class = StatusDriverSerializer
    permission_classes = [IsAuthenticated, IsClientOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)

