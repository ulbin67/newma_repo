from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.applycall),
    path("apply_box/",views.box_apply_call, name='box_apply_main'),
    path("create_apply/", views.box_apply_create, name='box_apply_create'),
    path("apply_check/", views.box_checkcall, name='apply_check'),
    path("managemain/", views.box_req),
    path("box_requsting/", views.box_going, name='manage'),
    path("sending_box/", views.sent_page),
    path("sending_box_create/", views.sent_apply_create, name='sent_apply_create'),
]