import os
import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.preprocessing import OneHotEncoder, StandardScaler, MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Input, LSTM, Dropout
import joblib
from .models import DoneApply

def 이번년도_달별박스수계산():
    current_year = datetime.now().year

    done_applies = DoneApply.objects.filter(done_at__year=current_year)

    monthly_box_counts = {}

    for apply in done_applies:
        month = apply.done_at.month
        if month not in monthly_box_counts:
            monthly_box_counts[month] = 0

        box_num = apply.box_num if apply.box_num is not None else 0
        monthly_box_counts[month] += box_num

    monthly_done_box_count = [
        {'month': month, 'total_box': total_box}
        for month, total_box in monthly_box_counts.items()
    ]

    data = monthly_done_box_count

    labels = [f"{datetime.now().year}-{item['month']:02}" for item in data]
    box_nums = [item['total_box'] for item in data]
    return labels, box_nums

def 상자_개수_추가_학습():
    current_year = datetime.now().year
    csv_name = f"{current_year}.csv"

    # CSV 파일에서 데이터 로드
    to_learn = pd.read_csv(csv_name)

    # 연도와 월을 분리
    to_learn['Year'] = to_learn['Month'].apply(lambda x: int(x.split('-')[0]))
    to_learn['Month'] = to_learn['Month'].apply(lambda x: int(x.split('-')[1]))

    X_new = to_learn[['Year', 'Month']]
    y_new = to_learn['Total Box']

    # 기존 전처리기 로드
    preprocessor = joblib.load('feature_scaler.pkl')
    
    # 기존 전처리기와 동일한 전처리 적용
    X_new_transformed = preprocessor.transform(X_new)

    # 모델 로드
    model = load_model('predict_model.h5')

    # 데이터가 충분한지 확인
    if len(X_new_transformed) < 2:
        print("데이터가 너무 적어 모델 학습을 진행할 수 없습니다.")
        return

    # 입력 데이터의 차원 변경
    X_new_transformed = X_new_transformed.reshape((X_new_transformed.shape[0], 1, X_new_transformed.shape[1]))

    # 모델 추가 학습
    model.fit(X_new_transformed, y_new, epochs=10, batch_size=1, validation_split=0.2, verbose=1)

    # 업데이트된 모델 저장
    model.save('predict_model.h5')
    print("모델이 추가 학습 후 저장되었습니다.")


def 상자_개수_예측():
    model = load_model('predict_model.h5')
    preprocessor = joblib.load('feature_scaler.pkl')
    target_scaler = joblib.load('target_scaler.pkl')

    current_year = datetime.now().year
    current_month = datetime.now().month

    # 다음 달 데이터 준비
    next_month = current_month + 1
    next_year = current_year

    if next_month > 12:
        next_month = 1
        next_year += 1

    df_next = pd.DataFrame({
        'Year': [next_year],
        'Month': [next_month]
    })

    # 다음 달의 데이터 전처리
    X_next_transformed = preprocessor.transform(df_next)
    X_next_transformed = X_next_transformed.reshape((X_next_transformed.shape[0], 1, X_next_transformed.shape[1]))

    # 다음 달의 예측 수행
    try:
        prediction_next_scaled = model.predict(X_next_transformed)
        prediction_next = target_scaler.inverse_transform(prediction_next_scaled)
    except Exception as e:
        print(f"예측 오류: {e}")
        return None, None

    # 결과 출력
    return f"{next_year}-{next_month:02}", prediction_next[0][0]