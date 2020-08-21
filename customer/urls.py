from django.conf.urls import url
from django.urls import path

from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()
# router.register('profile',views.CustomerViewSet)
# router.register('login',views.LogInView.as_view)
urlpatterns=[
    url(r'',include(router.urls)),
    url("profile",views.CustomerView.as_view()),
    url('login',views.LogInView.as_view())
]