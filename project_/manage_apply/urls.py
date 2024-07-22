from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.applycall),
    path("apply_box/",views.box_apply_call),
    path("apply_check/", views.box_apply_create, name='box_apply_create')

]