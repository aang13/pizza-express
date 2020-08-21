from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from phone_field import PhoneField
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

# Create your models here.

class customerManager(BaseUserManager):

    def create_user(self,mobile,password=None):
        if not mobile:
            raise ValueError('Please provide a valid mobile number')

        user=self.model(mobile=mobile)
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self,mobile,password):

        user=self.create_user(mobile,password)

        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)





class Customer(AbstractBaseUser,PermissionsMixin):
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255,unique=True)
    mobile=models.CharField(max_length=255,unique=True)
    address=models.TextField()
    current_location=models.PointField(geography=True, default=Point(0.0, 0.0))
    image=models.ImageField(null=True,max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=customerManager()

    USERNAME_FIELD='mobile'
    REQUIRED_FIELDS = []

    def __str__(self):
       return self.mobile

