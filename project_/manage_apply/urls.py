from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.applycall),
    path("apply_box/",views.box_apply_call, name='box_apply_main'),
    path("create_apply/", views.box_apply_create, name='box_apply_create'),
    path("apply_check/", views.box_checkcall, name='apply_check'),
    path("sending_box_create/", views.sent_apply_create, name='sent_apply_create'),
    path("save_failed_error", views.save_failed, name='failed'),
    path("researching_apply/",views.research_page_call, name='research_call'),
    path("researching_main/", views.research_apply, name='research'),
    path("pickreq_faild/",views.pick_failed, name='pick_failed'),
    path("pick_success/",views.req_success_call, name='request_sucess'),
    path("progess_research/",views.pro_research_call, name='progress_research'),
    path("progess_req/",views.research_apply2, name='research2'),
    path("<int:apply_id>/progress_check/", views.pro_check_call ,name='progress_check'),
]