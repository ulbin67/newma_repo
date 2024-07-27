from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.\

#기본 유저 정의
class User(AbstractUser):
    id = models.AutoField(primary_key=True, db_column='user_id')
    username = models.CharField(max_length=20, unique=True) #이게 아이디
    password = models.CharField(max_length=300, null=False)

    name = models.CharField(max_length=10, null=True)

    recent_address_num = models.CharField(max_length=5,null=True,blank=True)
    recent_address_info = models.TextField(null=True,blank=True)
    recent_address_detail = models.TextField(null=True,blank=True)
    recent_deli_request = models.TextField(null=True,blank=True)
    
    recent_company = models.CharField(max_length=10,null=True,blank=False)
    recent_num = models.CharField(max_length=14,null=True,blank=False,unique=True)
