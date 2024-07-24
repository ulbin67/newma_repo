from django import forms
from .models import apply
from .validators import phone_number_validate
from django.contrib.auth.forms import UserCreationForm

class ApplyForm(forms.ModelForm):
    class Meta:
        model = apply
        fields = [
            'company',
            'com_num',
            'applicant',
            'apcan_phone',
            'address_num',
            'address_info',
            'address_detail',
            'deli_request',
            'box_num',
        ]