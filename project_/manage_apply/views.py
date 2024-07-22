from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import box_apply
from django.views.generic import ListView,DetailView,UpdateView,CreateView

# Create your views here.

def applycall(request):
    return render(
        request,
        'manage_apply/apply_page.html'
    )

def box_apply_call(request):
    return render(
        request,
        "manage_apply/boxes_main.html"
    )

def box_apply_create(request):
    company = request.GET.get('company')
    com_num = request.GET.get('com_num')

    applicant = request.GET.get('applicant')
    apcan_phone = request.GET.get('apcan_phone')

    address_num = request.GET.get('sample6_postcode')
    address_info = request.GET.get('sample6_address')
    address_detail = request.GET.get('sample6_detailAddress')
    deli_request = request.GET.get('sample6_extraAddress')
    
    BOX_CREATE = box_apply(
        company=company,
        com_num=com_num,
        applicant=applicant,
        apcan_phone=apcan_phone,
        address_num=address_num,
        address_info=address_info,
        address_detail=address_detail,
        deli_request=deli_request
    )

    BOX_CREATE.save()

    return redirect("manage_apply/apply_check.html")