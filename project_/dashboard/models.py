from django.db import models

class ManageApplyCompanyInfo(models.Model):
    count = models.IntegerField()
    company = models.CharField(max_length=255)
    com_num = models.CharField(max_length=255)
    address_num = models.CharField(max_length=255)
    address_info = models.CharField(max_length=255)
    address_detail = models.CharField(max_length=255)
    recent_apply = models.DateField()
    recent_employee = models.DateField()

    class Meta:
        db_table = 'manage_apply_companyinfo'
        managed = False  # Django가 이 테이블의 스키마를 관리하지 않도록 설정

    def __str__(self):
        return self.company
