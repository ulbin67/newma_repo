<<<<<<< Updated upstream
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from .models import DoneApply
from django.utils import timezone

#모델에 저장된 값을 불러와 계산하는 쿼리 파일입니다.

def get_current_year_monthly_done_box_count():
    current_year = timezone.now().year  # 현재 연도 가져오기
    monthly_done_box_count = (
        DoneApply.objects
        .filter(done_at__year=current_year)  # 현재 연도의 데이터만 필터링
        .annotate(month=TruncMonth('done_at'))  # done_at 필드를 월 단위로 잘라냄
        .values('month')  # 월별로 그룹화
        .annotate(total_box=Sum('box_num'))  # 각 월별 box_num의 합계
        .order_by('month')  # 월별로 정렬
    )
    
    return monthly_done_box_count
=======
from datetime import datetime
from manage_apply.models import DoneApply
from django.db.models.functions import TruncMonth
from django.db.models import Sum


def 이번년도_달별박스수계산():
    current_datetime = datetime.now()
    current_year = current_datetime.year

    # 월별 박스 수 집계
    monthly_done_box_count = (
        DoneApply.objects
        .filter(done_at__year=current_year)
        .annotate(month=TruncMonth('done_at'))
        .values('month')
        .annotate(total_box=Sum('box_num'))
        .order_by('month')
    )
    
    labels = []
    box_nums = []

    for entry in monthly_done_box_count:
        labels.append(entry['month'].strftime('%Y-%m'))
        box_nums.append(entry['total_box'])
    
    return labels, box_nums
>>>>>>> Stashed changes
