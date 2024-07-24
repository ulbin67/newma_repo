from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class get_num(models.Model):
    got_num = models.CharField(max_length=11,null=True,blank=False)

#박스 요청 및 수거 date 틀
class apply(models.Model):
    #모델 생성 시 오류를 없애기 위해 null=True로 지정 (값이 null이어도 됨, 추후 추가된 칼럼의 경우 자동으로 null값이 생겨서 오류 발생..)
    #신청 시간
    pk = True
    
    apply_at = models.DateTimeField(auto_now_add=True,null=True)

    #회사 정보
    company = models.CharField(max_length=10,null=True,blank=False,unique=True)
    com_num = models.CharField(max_length=14,null=True,blank=True)

    #주소
    address_num = models.CharField(max_length=5,null=True,blank=True,unique=True)
    address_info = models.TextField(null=True,blank=True)
    address_detail = models.TextField(null=True,blank=True)
    deli_request = models.TextField(null=True,blank=True)
    
    #신청자 정보
    applicant = models.CharField(max_length=10, null=True, blank=False)
    apcan_phone = models.CharField(max_length=14,null=True,blank=False,unique=True)
   

    PROGRESS_RATE = (
    	(0, '박스 요청중'),
        (1, '박스 전송중'),
        (2, '박스 수거 요청중'),
        (3, '수거진행중'),
        (4, '수거완료'),
    )

    #진행사항
    progress = models.CharField(max_length=2,choices=PROGRESS_RATE, default=0, null=True)

    #박스 수
    box_num = models.IntegerField(null=True,blank=False)

    #송장 번호
    invoice_numberaddress_num = models.TextField(null=True,blank=False)

    #박스 요청 없이 오는 경우의 연결
    zir_block_kg = models.FloatField(null=True, blank=True)
    zir_block_count = models.IntegerField(null=True, blank=True)

    #지르코니아 분말
    zir_powder_kg = models.FloatField(null=True, blank=True)
    zir_powder_count = models.IntegerField(null=True, blank=True)

    #환봉
    round_bar_kg = models.FloatField(null=True, blank=True)
    round_bar_count = models.IntegerField(null=True, blank=True)

    #밀링툴
    tool_kg = models.FloatField(null=True, blank=True)
    tool_count = models.IntegerField(null=True, blank=True)

    #개인 요청에 따른 주소를 만드는 함수
    def get_absolute_url(self):
        return f'applymain/applycheck/{self.pk}'
    
    def del_absolute_url(self):
        return f'applymain/sending_box/{self.pk}'
    
class company_info(models.Model):
    #회사 정보
    company = models.CharField(max_length=10,null=True,blank=False,unique=True)
    com_num = models.CharField(max_length=14,null=True,blank=True)

    #주소
    address_num = models.CharField(max_length=5,null=True,blank=True,unique=True)
    address_info = models.TextField(null=True,blank=True)
    address_detail = models.TextField(null=True,blank=True)
    deli_request = models.TextField(null=True,blank=True)

    #회사 최근 거래자 & 거래 시각 파악
    resent_apply = models.DateTimeField(auto_now = True,null=True)
    resent_employee = models.CharField(max_length=10, null=True, blank=False)