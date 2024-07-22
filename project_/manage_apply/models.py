from django.db import models
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

#박스 요청 및 수거 date 틀
class box_apply(models.Model):
    #모델 생성 시 오류를 없애기 위해 null=True로 지정 (값이 null이어도 됨, 추후 추가된 칼럼의 경우 자동으로 null값이 생겨서 오류 발생..)
    #신청 시간
    apply_at = models.DateTimeField(auto_now_add=True,null=True)

    #회사 정보
    company = models.CharField(max_length=10,null=True,blank=False)
    com_num = models.CharField(max_length=11,null=True,blank=True)

    #신청자 정보
    applicant = models.CharField(max_length=10, null=True, blank=False)
    apcan_phone = models.CharField(max_length=11,null=True,blank=False)

    #주소 정보
    address_num = models.CharField(max_length=5,null=True,blank=False)
    address_info = models.TextField(null=True,blank=False)
    address_detail = models.TextField(null=True,blank=False)
    deli_request = models.TextField(null=True,blank=False)

    PROGRESS_RATE = (
    	('0', '박스 요청중'),
        ('1', '박스 전송중'),
        ('2', '박스 수거 요청중'),
        ('3', '수거진행중'),
        ('4', '수거완료'),
    )

    #진행사항
    progress = models.CharField(max_length=2,choices=PROGRESS_RATE, default='0', null=True)


    #송장 번호
    invoice_numberaddress_num = models.TextField(null=True,blank=False)
