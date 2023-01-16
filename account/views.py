from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from service.models import StatusDriver
from service.permissions import IsClientOrReadOnly
from service.serializers import StatusDriverSerializer
from .serializers import ProfileRegisterSerializer
from .models import Profile, User


class ProfileListAPIView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileRegisterSerializer

    def create_profile(self, request, is_driver):
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid():
            serializer.save(is_driver=is_driver)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=False, url_path='register/driver')
    def driver(self, request, pk=None):
        return self.create_profile(request, True)

    @action(methods=['post'], detail=False, url_path='register/passenger')
    def passenger(self, request, pk=None):
        return self.create_profile(request, False)

    @action(methods=['post'], detail=False, permission_classes=[IsClientOrReadOnly, ])
    def leave_status(self, request, pk=None):
        serializer = StatusDriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(profile=request.user.profile)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'], detail=False)
    def view_statuses(self, request, pk=None):
        queryset = StatusDriver.objects.all()
        serializer = StatusDriverSerializer(queryset, many=True)

        return Response(serializer.data)







