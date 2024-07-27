from django.urls import path
from . import views

urlpatterns = [
    path("qna/", views.faq_list, name='faq_list'),
    path('faq/<int:pk>/', views.faq_detail, name='faq_detail'),
]

