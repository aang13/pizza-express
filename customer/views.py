from django.http import Http404
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from customer.serializers import CustomerSerializer
from .models import  Customer
from . import serializers
from . import models


# Create your views here.

class CustomerView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    def get(self,request):
        try:
            customer_profile=Customer.objects.get(mobile=request.user)
            status_code=status.HTTP_200_OK
            response = {
                "name": customer_profile.name,
                "phone": customer_profile.mobile,
                "address": customer_profile.address,
            }
        except Exception as e:
            status_code = status.HTTP_401_UNAUTHORIZED
            response = {
                'msg': 'User does not exists',
                'error': str(e)
                }

        return Response(response, status=status_code)
    def patch(self,request):
        customer_profile=Customer.objects.get(mobile=request.user)
        serializer=CustomerSerializer(customer_profile,data=request.data)
        if serializer.is_valid():
            serializer.save()
            response={
                "msg":"OK"
            }
            status_code=status.HTTP_200_OK
            return Response(response,status=status_code)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LogInView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.LogInSerializer

    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response={
            # 'name': serializer.data['name'],
            'phone':serializer.data['mobile'],
            'jwt_token':serializer.data['jwt_token'],
            'status code': status.HTTP_200_OK,
        }
        status_code=status.HTTP_200_OK

        return Response(response,status=status_code)