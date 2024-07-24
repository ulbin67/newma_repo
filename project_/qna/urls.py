

from django.urls import path
from . import views

urlpatterns = [
    path("qna/", views.faq_list, name='faq_list'),
]

