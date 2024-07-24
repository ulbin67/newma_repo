from django import forms
from .models import apply
from .validators import phone_number_validate

class ApplyForm(forms.ModelForm):
    company = forms.CharField(max_length=10, unique=True)
    com_num = forms.CharField(max_length=11)

    #주소
    address_num = forms.CharField(max_length=5)
    address_info = forms.TextField()
    address_detail = forms.TextField()
    deli_request = forms.TextField()
    
    #신청자 정보
    applicant = forms.CharField(max_length=10)
    apcan_phone = forms.CharField(max_length=11)

    #박스 수
    box_num = forms.IntegerField()