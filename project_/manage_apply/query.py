from datetime import datetime
from manage_apply.models import DoneApply
from django.db.models.functions import ExtractMonth
from django.db.models import Sum


def 이번년도_달별박스수계산():
    current_year = datetime.now().year

    # 현재 연도의 데이터만 필터링
    done_applies = DoneApply.objects.filter(done_at__year=current_year)

    # 월별 박스 수를 계산하기 위한 딕셔너리
    monthly_box_counts = {}

    for apply in done_applies:
        month = apply.done_at.month
        if month not in monthly_box_counts:
            monthly_box_counts[month] = 0
        monthly_box_counts[month] += apply.box_num

    # 딕셔너리를 리스트로 변환하여 반환
    monthly_done_box_count = [
        {'month': month, 'total_box': total_box}
        for month, total_box in monthly_box_counts.items()
    ]

    return monthly_done_box_count

def process_monthly_done_box_count():
    data = 이번년도_달별박스수계산()
    labels = [f"{datetime.now().year}-{item['month']:02}" for item in data]
    box_nums = [item['total_box'] for item in data]
    return labels, box_nums