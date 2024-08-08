from django.db import models


class ManageApplyCompanyInfo(models.Model):
    count = models.PositiveIntegerField()  # 양수만 허용하는 필드로 변경
    company = models.CharField(max_length=10)
    com_num = models.CharField(max_length=14)
    address_num = models.CharField(max_length=5)
    address_info = models.TextField()  # LongText는 TextField로 매핑
    address_detail = models.TextField()
    recent_apply = models.DateTimeField()  # datetime으로 변경
    recent_employee = models.CharField(max_length=10)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        db_table = 'manage_apply_companyinfo'
        managed = False  # Django가 이 테이블의 스키마를 관리하지 않도록 설정

    def __str__(self):
        return self.company
