import re
from django.forms import ValidationError

REGEX_PHONE_NUMBER = '\d{3}-\d{3,4}-\d{4}'

def phone_number_validate(phone_number):
    if not re.match(REGEX_PHONE_NUMBER, phone_number):
                raise ValidationError("전화번호 양식이 맞지 않습니다.")