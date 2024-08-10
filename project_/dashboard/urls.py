from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),  # 홈 페이지에 연결
    # path('map/', views.map_view, name='map_view'), # 이 줄을 제거하거나 주석 처리합니다.
]
