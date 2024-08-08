
# 네이버로 지오코딩하고, sql테이블에 그 결과를 저장, 결과값으로 지도에 마커

import folium
from django.shortcuts import render
from django.db import models
from .models import ManageApplyCompanyInfo
import requests
from django.db import transaction

# 네이버 API 설정
# 박가현 개인 키입니다.. 나중에 사업자 아이디 키로 바꾸죠..
# 테이블에 저장해서 쓰는거라 사용량 괜찮을듯..
NAVER_CLIENT_ID = 'ahkymw2inp'  # 네이버 클라이언트 ID
NAVER_CLIENT_SECRET = 'NTm1ZKbQNC6ZeJS55NqRrLj2rKQuGGMgS9REvpD4'  # 네이버 클라이언트 시크릿

def get_naver_geocode(address):
    url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"
    headers = {
        "X-NCP-APIGW-API-KEY-ID": NAVER_CLIENT_ID,
        "X-NCP-APIGW-API-KEY": NAVER_CLIENT_SECRET
    }
    params = {
        "query": address
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        #API 응답에 대한 내용 출력 확인용
        #print(f"API Response Status: {response.status_code}, Content: {response.text}")

        if response.status_code == 200:
            data = response.json()
            if 'addresses' in data and data['addresses']:
                latitude = data['addresses'][0]['y']
                longitude = data['addresses'][0]['x']
                return float(latitude), float(longitude)
            else:
                #지오코딩 데이터 못찾았을때
                print(f"No geocode data found for {address}")
                return None, None
        # else:
        #     #에러났을 때
        #     print(f"Error {response.status_code}: {response.text}")
        #     return None, None
    except requests.exceptions.RequestException as e:
        print(f"Request exception: {e}")
        return None, None

def dashboard_home(request):
    # 지도 생성: 대한민국 중심 좌표
    m = folium.Map(location=[36.5, 127.5], zoom_start=7, tiles='CartoDB positron')

    # 지오코딩이 필요한 데이터 가져오기
    companies_to_geocode = ManageApplyCompanyInfo.objects.filter(
        models.Q(latitude__isnull=True) | models.Q(longitude__isnull=True) | models.Q(latitude=0.0) | models.Q(longitude=0.0)
    )

    # 지오코딩 및 데이터베이스 업데이트
    with transaction.atomic():
        for company in companies_to_geocode:
            address = company.address_info  # 도로명주소
            print(f"Geocoding address: {address}")  # 주소 출력
            if not address:
                print("주소란이 비었습니다.")
                continue

            try:
                latitude, longitude = get_naver_geocode(address)
                if latitude is not None and longitude is not None:
                    # 데이터베이스 업데이트 전 로그 출력
                    #print(f"Updating {company.company} with Latitude: {latitude}, Longitude: {longitude}")
                    
                    # 모델 필드 업데이트
                    company.latitude = latitude
                    company.longitude = longitude
                    company.save()  # 업데이트 저장

                    # 저장 후 로그 출력
                    print(f"Updated {company.company}: Latitude {company.latitude}, Longitude {company.longitude}")
                else:
                    print(f"Geocode failed for {address}")
            except Exception as e:
                print(f"Error geocoding {address}: {e}")

    # 모든 회사 정보를 가져와 지도에 마커 추가
    all_companies = ManageApplyCompanyInfo.objects.all()
    for company in all_companies:
        if company.latitude is not None and company.longitude is not None:
            popup = folium.Popup(f"{company.company}", max_width=150)

            folium.Marker(
                [company.latitude, company.longitude],
                popup=popup  # 마커 위치
                #tooltip=company.company  # 마커 위 마우스 올릴 때 나타나는 툴팁
            ).add_to(m)
            
            #print(f"Marker added: {company.company} at {company.latitude}, {company.longitude}")

    # 지도를 HTML 문자열로 변환
    map_html = m._repr_html_()

    return render(request, 'dashboard/home.html', {'map_html': map_html})