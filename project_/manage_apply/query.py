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
