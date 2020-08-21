from rest_framework import serializers
from django.contrib.auth import authenticate

from . import models
from rest_framework_jwt.settings import api_settings

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Customer
        fields=('id','email','name','mobile','address','password')
        extra_kwargs={'password':{'write_only':True}}

        def create(selfs,validated_data):
            customer=models.Customer(
                email=validated_data['email'],
                mobile=validated_data['mobile'],
                # name=validated_data['name']
            )
            customer.set_password(validated_data['password'])
            customer.save()

            return customer


class LogInSerializer(serializers.Serializer):
    mobile=serializers.CharField(max_length=20)
    # name=serializers.CharField(max_length=255)
    password=serializers.CharField(max_length=255,write_only=True)
    jwt_token=serializers.CharField(max_length=255,read_only=True)

    def validate(self,data):
        mobile=data.get("mobile",None)
        password=data.get("password",None)
        user=authenticate(mobile=mobile,password=password)

        if user is None:
            raise serializers.ValidationError(
                'No user found with this mobile and password'
            )
        try:
            payload=JWT_PAYLOAD_HANDLER(user)
            jwt_token=JWT_ENCODE_HANDLER(payload)
        except models.Customer.DoesNotExist:
            raise serializers.ValidationError(
                'user with given mobile and password deos not exists'
            )
        return {
            'name':user.name,
            'mobile':user.mobile,
            'jwt_token':jwt_token
        }