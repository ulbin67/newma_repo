import os
import numpy as np
import pandas as pd
from datetime import datetime
import joblib
from .models import DoneApply, Apply
from django.conf import settings
from django.db.models import Sum

def 달별박스수계산():
    # 현재 연도를 가져옵니다.
    current_year = datetime.now().year

    # DoneApply 모델에서 월별로 box_num의 합계를 계산합니다.
    monthly_box_counts = DoneApply.objects.filter(
        done_at__year=current_year
    ).values('done_at__month').annotate(
        total_box=Sum('box_num')
    ).order_by('done_at__month')

    # 월별 상자 수 데이터를 준비합니다.
    monthly_done_box_count = [
        {'month': entry['done_at__month'], 'total_box': entry['total_box'] or 0}
        for entry in monthly_box_counts
    ]

    # 레이블과 상자 수를 추출합니다.
    labels = [f"{current_year}-{item['month']:02}" for item in monthly_done_box_count]
    box_nums = [item['total_box'] for item in monthly_done_box_count]
    
    return labels, box_nums