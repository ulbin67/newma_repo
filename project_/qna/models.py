from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.



class Post(models.Model):
    postname = models.CharField(max_length=50)
    # 게시글 Post에 이미지 추가
    mainphoto = models.ImageField(blank=True, null=True)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    answer = models.TextField(null=True,blank=True)
    password = models.PositiveBigIntegerField()

    # 게시글의 제목
    def __str__(self):
        return self.postname
    
