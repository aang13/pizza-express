from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns=[
    path('pizza/',views.PizzaList.as_view()),
    path('pizza/<int:pk>/',views.PizzaDetail.as_view()),
    path('order/',views.OrderList.as_view()),
    path('order/<int:pk>/',views.OrderDetail.as_view()),
]