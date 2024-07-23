from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import apply
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

def box_checkcall(request):
    return render(
        request,
        "manage_apply/apply_check.html"
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

    box_num = request.GET.get('box_num')
    
    BOX_CREATE = apply(
        company=company,
        com_num=com_num,
        applicant=applicant,
        apcan_phone=apcan_phone,
        address_num=address_num,
        address_info=address_info,
        address_detail=address_detail,
        deli_request=deli_request,
        box_num = box_num
    )
    BOX_CREATE.save()
    return redirect('apply_check')

def manage_main(request):
    return render(
        request,
        'manage_apply/manage_page.html',
    )


def box_req(request):
    apply_list = apply.objects.all(),
    return render(
        request,
        'manage_apply/manage_page.html',
        {
            'applys' : apply_list,
        }
    )

def box_going(request):
    apply_list = apply.objects.filter(progress=0),
    return render(
        request,
        'manage_apply/manage_box_reqing.html',
        {
            'applys' : apply_list,
        }
    )

def pic_req(request):
    apply_list = apply.objects.filter(progress=2),
    return render(
        request,
        'manage_apply/manage_page0.html',
        {
            'applys' : apply_list,
        }
    )

def sent_page(request):
    return render(
        request,
        'manage_apply/sent_box.html',
    )

def sent_apply_create(request):

    zir_block_kg = request.GET.get("z_b_kg")
    zir_block_count = request.GET.get("z_b_num")

    zir_powder_kg = request.GET.get("z_p_kg")
    zir_powder_count = request.GET.get("z_p_num")
    
    round_bar_kg = request.GET.get("r_b_kg")
    round_bar_count = request.GET.get("r_b_num")

    tool_kg = request.GET.get("tool_kg")
    tool_count = request.GET.get("tool_num")

    box_num = int(zir_block_count) + int(zir_powder_count) + int(round_bar_count) + int(tool_count)

    progress = 3

    company = request.GET.get('company')
    com_num = request.GET.get('com_num')

    applicant = request.GET.get('applicant')
    apcan_phone = request.GET.get('apcan_phone')
    invoice_numberaddress_num = request.GET.get('invoice_num')

    SENT_CREATE = apply(
        zir_block_kg = zir_block_kg,
        zir_block_count = zir_block_count,
        zir_powder_kg = zir_powder_kg,
        zir_powder_count = zir_powder_count,
        round_bar_kg = round_bar_kg,
        round_bar_count = round_bar_count,
        tool_kg = tool_kg,
        tool_count = tool_count,
        box_num = box_num,
        progress = progress,
        company = company,
        com_num = com_num,
        applicant = applicant,
        apcan_phone = apcan_phone,
        invoice_numberaddress_num = invoice_numberaddress_num,
    )

    SENT_CREATE.save()

    return redirect('apply_check')