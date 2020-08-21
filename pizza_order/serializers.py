from rest_framework import serializers

from . import models

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Pizza
        fields=('id','name','brand','price','weight','availability')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Order
        fields=('id','pizza''customer','quantity','order_price','order_state','delivery_time')
