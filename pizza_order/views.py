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
# class PizzaViewSet(viewsets.ModelViewSet):
#     serializer_class = serializers.PizzaSerializer
#     queryset = Pizza.objects.all()
#     permission_classes = (AllowAny,)

class PizzaList(APIView):
    def get(self,request,format=None):
        pizzas=Pizza.objects.all()
        serializer=PizzaSerializer(pizzas,many=True)
        return Response(serializer.data)


class PizzaDetail(APIView):

    def get_object(self,pk):
        try:
            return Pizza.objects.get(pk=pk)
        except Pizza.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        pizza=self.get_object(pk)
        serializer=PizzaSerializer(pizza)
        return Response(serializer.data)


# class OrderViewSet(viewsets.ModelViewSet):
#     serializer_class = serializers.OrderSerializer
#     queryset = Order.objects.all()
#     permission_classes = (IsAuthenticated,)
#     authentication_classes = JSONWebTokenAuthentication


class OrderList(APIView):
    def get(self,request,format=None):
        orders=Order.objects.all()
        serializer=OrderSerializer(orders,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer=OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetail(APIView):

    def get_object(self,pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        order=self.get_object(pk)
        serializer=PizzaSerializer(order)
        return Response(serializer.data)