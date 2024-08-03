from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.maincall, name='home'),
    path("introduce_newma/", views.introcall),
    path("information_newma/",views.infocall),

    # localhost/logout -> 로그아웃 기능
    path("logout/", views.logout_view, name='logout'),

    # localhost/accounts/register -> 회원가입
    path("accounts/register/",views.UserCreateView.as_view(), name="register"),

    # localhost/accounts/register/checkid -> 아이디 중복 검사(회원가입에서 진행)
    path("accounts/register/checkid/", views.UserIdCheckView.as_view(), name="check_id"),

    # localhost/acounts/register/done : 회원가입 성공시 사용
    path("accounts/register/success",views.UserCreateDoneTV.as_view(), name="register_done")
]