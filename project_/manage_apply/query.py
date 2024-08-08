import os
import numpy as np
import pandas as pd
from datetime import datetime
from manage_apply.models import DoneApply
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Input
import joblib

def 이번년도_달별박스수계산():
    current_year = datetime.now().year

    done_applies = DoneApply.objects.filter(done_at__year=current_year)

    monthly_box_counts = {}
    for apply in done_applies:
        month = apply.done_at.month
        if month not in monthly_box_counts:
            monthly_box_counts[month] = 0
        monthly_box_counts[month] += apply.box_num

    monthly_done_box_count = [
        {'month': month, 'total_box': total_box}
        for month, total_box in monthly_box_counts.items()
    ]

    data = monthly_done_box_count

    labels = [f"{datetime.now().year}-{item['month']:02}" for item in data]
    box_nums = [item['total_box'] for item in data]
    return labels, box_nums
    

def 상자_개수_학습():
    current_year = datetime.now().year
    csv_name = f"{current_year}.csv"

    months, nums = 이번년도_달별박스수계산()

    if not months:
        print("현재 연도의 데이터가 없습니다. CSV 파일을 저장하지 않습니다.")
        return
    
    years = [current_year] * len(months)
    year_months = [f"{current_year}_{month:02}" for month in [int(m.split('-')[1]) for m in months]]

    df = pd.DataFrame({'YMs': year_months, 'Year': years, 'Month': months, 'Total Box': nums})

    df.to_csv(csv_name, index=False)
    print(f"{csv_name} 파일이 성공적으로 저장되었습니다.")

    to_learn = pd.read_csv(csv_name)

    X = to_learn[['YMs', 'Year', 'Month']]
    y = to_learn['Total Box']

    preprocessor = ColumnTransformer(
        transformers=[
            ('year_month', OneHotEncoder(), ['YMs']),
            ('year', 'passthrough', ['Year']),
            ('month', 'passthrough', ['Month'])
        ],
        remainder='drop'
    )

    X_transformed = preprocessor.fit_transform(X)

    # Check if there is enough data
    if len(X_transformed) < 2:
        print("데이터가 너무 적어 모델 학습을 진행할 수 없습니다.")
        return

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=42)

    # Define and train the model
    model = Sequential([
        Input(shape=(X_transformed.shape[1],)),
        Dense(64, activation='relu'),
        Dense(32, activation='relu'),
        Dense(1)
    ])

    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(X_train, y_train, epochs=10, batch_size=1, validation_data=(X_test, y_test))

    model.save('predict_model.h5')
    joblib.dump(preprocessor, 'preprocessor.pkl')

def 상자_개수_예측():
    model = load_model('predict_model.h5')
    preprocessor = joblib.load('preprocessor.pkl')

    current_year = datetime.now().year
    current_month = datetime.now().month
    next_month = current_month + 1
    next_year = current_year

    if next_month > 12:
        next_month = 1
        next_year += 1

    year_months = [f"{current_year}_{current_month:02}", f"{next_year}_{next_month:02}"]
    years = [current_year, next_year]
    months = [current_month, next_month]

    df = pd.DataFrame({
        'YMs': year_months,
        'Year': years,
        'Month': months
    })

    X_transformed = preprocessor.transform(df)

    predictions = model.predict(X_transformed)

    for ym, pred in zip(year_months, predictions):
        print(f"{ym}: 예측된 박스 수는 {pred[0]:.2f}")

    return year_months, predictions.flatten()