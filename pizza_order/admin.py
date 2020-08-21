
from django.contrib import admin
from pizza_order.models import  Pizza,Order,Tag
# Register your models here.
admin.site.register(Pizza)
admin.site.register(Order)
admin.site.register(Tag)