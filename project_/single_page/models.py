from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.\

#기본 유저 정의
class User(AbstractUser):
    name = models.CharField(max_length=10, null=True)
    address_num = models.CharField(max_length=5, null=True, blank=True)
    address_info = models.TextField(null=True, blank=True)
    address_detail = models.TextField(null=True, blank=True)
    deli_request = models.TextField(null=True,blank=True)
    phone_num = models.CharField(max_length=14,null=True,blank=False)
    company_name = models.CharField(max_length=100, null=True,blank=True)

