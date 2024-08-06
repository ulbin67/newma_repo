import folium
from django.shortcuts import render
from .models import ManageApplyCompanyInfo
from geopy.geocoders import Nominatim
from folium.plugins import MarkerCluster

def dashboard_home(request):
    # 지도 생성: 대한민국 중심 좌표
    m = folium.Map(location=[36.5, 127.5], zoom_start=7, tiles='CartoDB positron')

    # Geopy 지오코더 초기화
    geolocator = Nominatim(user_agent="geoapiExercises")

    # 모든 회사 정보 가져오기
    companies = ManageApplyCompanyInfo.objects.all()

    # MarkerCluster 생성
    marker_cluster = MarkerCluster().add_to(m)

    # 각 회사 위치에 마커 추가
    for company in companies:
        address = f"{company.address_info}" # 도로명주소 + 건물번호
        # address = f"{company.address_info} {company.address_detail}" 상세주소포함,, 근데 필요없을듯
        try:
            # 주소를 위도, 경도로 변환
            # 지오코딩 서비스에 대해 상업적 사용 가능한 API들로 교체 필요성 검토 (네이버, 카카오 등)(*상업적 사용 유료)
            # 현재 테스트용으로 설정한 Geopy 라이브러리 지오코더는 변환 실패할때도 성공할때도 있어서..... 바꿔야됨!
            # 그리고 비상업적용도로만 사용 가능
            location = geolocator.geocode(address, timeout=10) #자꾸 오류나서 timeout 추가 ㅜㅜ, 유료로 바꿔야할듯
            if location:
                folium.Marker(
                    [location.latitude, location.longitude],
                    popup=f"{company.company}",
                    tooltip=company.company
                ).add_to(marker_cluster)
                print(f"Marker added: {company.company} at {location.latitude}, {location.longitude}")
            else: #위도, 경도 변환 실패한 주소가 있을시, 해당 주소 로그로 나타내줌
                print(f"Geocode failed for {address}")
        except Exception as e:
             print(f"Error geocoding {address}: {e}")
       

    # 지도를 HTML 문자열로 변환
    map_html = m._repr_html_()

    return render(request, 'dashboard/home.html', {'map_html': map_html})
