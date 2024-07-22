from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.applycall),
    path("apply_box/",views.box_apply_call),
    path("create_apply/", views.box_apply_create, name='box_apply_create'),
    path("apply_check/", views.box_checkcall, name='apply_check'),
]