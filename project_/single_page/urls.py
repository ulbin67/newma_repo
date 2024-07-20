from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.maincall),
    path("introduce_newma/", views.introcall),
    path("information_newma/",views.infocall),

]