from django.http import Http404
from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.views import APIView
from pizza_order.serializers import PizzaSerializer,OrderSerializer
from rest_framework import viewsets
from . import serializers
from .models import Pizza,Order
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class PizzaList(APIView):
    permission_classes = (AllowAny,)
    def get(self,request,format=None):
        pizzas=Pizza.objects.all()
        serializer=PizzaSerializer(pizzas,many=True)
        return Response(serializer.data)


class PizzaDetail(APIView):
    permission_classes = (AllowAny,)
    def get_object(self,pk):
        try:
            return Pizza.objects.get(pk=pk)
        except Pizza.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        pizza=self.get_object(pk)
        serializer=PizzaSerializer(pizza)
        return Response(serializer.data)



class OrderList(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    def get(self,request,format=None):
        orders=Order.objects.all()
        serializer=OrderSerializer(orders,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer=OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response={
                "msg":"OK"
            }
            return Response(response,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetail(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get_object(self,pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        order=self.get_object(pk)
        serializer=PizzaSerializer(order)
        return Response(serializer.data)