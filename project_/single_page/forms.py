from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


# 기본 사용자 생성 폼을 확장한 커스텀 사용자 생성 폼
class CustomUserCreationForm(UserCreationForm):
    # 전화번호 부분을 위한 추가 필드 정의
    phone_telecom = forms.CharField(max_length=7, required=True)
    phone_part1 = forms.CharField(max_length=3, required=True)
    phone_part2 = forms.CharField(max_length=4, required=True)
    phone_part3 = forms.CharField(max_length=4, required=True)

    class Meta(UserCreationForm.Meta):
        # 커스텀 User 모델 사용
        model = User
        # 폼에 포함할 필드들
        fields = ('username', 'password1', 'password2', 'name', 'address_num',
                  'address_info', 'address_detail', 'deli_request')

        # 특정 필드의 외관을 커스터마이징하기 위해 위젯 정의
        widgets = {
            'address_info': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'address_detail': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'deli_request': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
        }

    # 저장 메서드를 재정의하여 전화번호 부분을 하나의 필드로 결합
    def save(self, commit=True):
        user = super().save(commit=False)
        # 전화번호 부분을 하나의 문자열로 결합
        phone_num = f"{self.cleaned_data['phone_part1']}-{self.cleaned_data['phone_part2']}-{self.cleaned_data['phone_part3']}"
        # 결합된 전화번호를 사용자 인스턴스에 할당
        user.phone_num = phone_num
        if commit:
            # 사용자 인스턴스를 데이터베이스에 저장
            user.save()
        return user


# 중복 사용자 ID 확인 폼
class CheckForm(forms.Form):
    check_id = forms.CharField(label='아이디 확인')