from django.db import models
from customer.models import Customer
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
ORDER_STATUS=(
    ("submitted","submitted"),
    ("confirmed", "confirmed"),
    ("cancelled", "cancelled"),
    ("delivered","delivered"),
)


# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=255)


class Pizza(models.Model):
    name=models.CharField(max_length=255)
    brand=models.CharField(max_length=255,unique=True)
    availability=models.BooleanField(default=True)
    price=models.DecimalField(max_digits=16,decimal_places=6)
    weight=models.DecimalField(max_digits=16,decimal_places=6)
    image=models.ImageField(max_length=255)
    tags=models.ForeignKey(Tag,null=True,on_delete=models.CASCADE)


class Order(models.Model):
    pizza=models.ForeignKey(Pizza,on_delete=models.CASCADE,null=True, related_name='pizza')
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True ,related_name='customer')
    quantity=models.IntegerField()
    order_price=models.DecimalField(max_digits=16,decimal_places=6)
    address=models.TextField(max_length=255)
    location=models.PointField(geography=True, default=Point(0.0, 0.0))
    order_state=models.CharField(max_length=20,choices=ORDER_STATUS)
    delivery_time=models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self