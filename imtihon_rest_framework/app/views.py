from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializer import *

class SuvViewSet(ModelViewSet):
    queryset = Suv.objects.all()
    serializer_class = SuvSerializer

class MijozViewSet(ModelViewSet):
    queryset = Suv.objects.all()
    serializer_class = MijozSerializer

class AdminView(APIView):
    def get(self, request, a=None):
        if a==None:
            admins = Admin.objects.all()
            ser = AdminSerializer(admins, many=True)
            return Response(ser.data, status=status.HTTP_200_OK)
        else:
            admins = Admin.objects.get(id=a)
            ser = AdminSerializer(admins)
            return Response(ser.data, status=status.HTTP_200_OK)

class HaydovchiView(APIView):
    def get(self, request, a=None):
        if a==None:
            users = Haydovchi.objects.all()
            ser = HaydovchiSerializer(users, many=True)
            return Response(ser.data, status=status.HTTP_200_OK)
        else:
            users = Haydovchi.objects.get(id=a)
            ser = HaydovchiSerializer(users)
            return Response(ser.data, status=status.HTTP_200_OK)

class BuyurtmaView(APIView):
    def get(self, request, a=None):
        if a==None:
            users = Haydovchi.objects.all()
            ser = HaydovchiSerializer(users, many=True)
            return Response(ser.data)
        else:
            user = Haydovchi.objects.get(id=a)
            ser = HaydovchiSerializer(user)
            return Response(ser.data, status=status.HTTP_200_OK)
    def post(self, request):
        b = BuyurtmaSerializer(data=request.data)
        if b.is_valid():
            b.save()
            return Response(b.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
