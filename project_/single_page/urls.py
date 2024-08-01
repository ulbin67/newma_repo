from django.urls import path,include
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("", views.maincall, name='home'),
    path("introduce_newma/", views.introcall),
    path("information_newma/",views.infocall),

    path("accounts/", include('django.contrib.auth.urls')),

    # localhost/accounts/custom_logout/  : 로그아웃 완료
    path('accounts/custom_logout/', LogoutView.as_view(template_name='registration/custom_logged_out.html'), name='logout'),

    # localhost/accounts/register : 회원가입
    path("accounts/register/",views.UserCreateView.as_view(), name="register"),

    # localhost/accounts/register/checkid : 회원가입 >> 아이디 중복 검사
    path("accounts/register/checkid/", views.UserIdCheckView.as_view(), name="check_id"),

    # localhost/acounts/register/done : 회원가입 성공시 사용
    path("accounts/register/success",views.UserCreateDoneTV.as_view(), name="register_done"),

    # localhost/accounts/search_id/   : 아이디 찾기
    path("accounts/search_id/", views.SearchIdView.as_view(), name='search_id'),

    # localhost/accounts/search_id/success/  : 아이디 찾기 성공
    path("accounts/search_id/success/", views.SearchIdDoneTV.as_view(), name='search_id_done'),

    # localhost/accounts/search_psw/  : 비밀번호 찾기 메인
    path("accounts/search_psw/", views.SearchPswView.as_view(), name='search_psw'),

    # localhost/accounts/search_psw/update/  : 비밀번호 재설정
    path("accounts/search_psw/update", views.UpdatePswView.as_view(), name='update_psw'),

    # localhost/accounts/search_psw/success/  : 비밀번호 재설정 성공
    path("accounts/search_psw/success/", views.UpdatePswDoneTV.as_view(), name='update_psw_done'),

    # localhost/accounts/my_page/   : 마이페이지
    path("accounts/my_page/", views.MyPageView.as_view(), name='my_page'),

    # localhost/accounts/my_page/confirm/  : 내 정보 수정 전 회원 확인
    path("accounts/my_page/confirm/", views.ConfirmInfoView.as_view(), name='confirm_my_info'),

    # localhost/accounts/my_page/info/   : 내 정보 수정
    path("accounts/my_page/info/", views.UpdateMyInfoView.as_view(), name='update_info'),

    # localhost/accounts/my_page/info/delete   : 회원 탈퇴 기능
    path("accounts/my_page/info/delete", views.DeleteMyInfoView.as_view(), name='delete_info'),

]