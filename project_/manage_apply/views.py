from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import apply,company_info,get_num
from django.views.generic import ListView,DetailView,UpdateView,CreateView
import re

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
    try:
        # 정규표현식으로 공백 제거
        company = re.sub(r'[\s]', '', request.POST.get('company', ''))
        # 숫자만 저장
        com_num = re.sub(r'[^0-9]', '', request.POST.get('com_num', ''))
        # 공백 제거
        applicant = re.sub(r'[\s]', '', request.POST.get('applicant', ''))
        # 숫자만 저장
        apcan_phone = re.sub(r'[^0-9]', '', request.POST.get('apcan_phone', ''))

        address_num = request.POST.get('sample6_postcode', '')
        address_info = request.POST.get('sample6_address', '')
        address_detail = request.POST.get('sample6_detailAddress', '')
        deli_request = request.POST.get('sample6_extraAddress', '')

        box_num = request.POST.get('box_num', '')

        # 회사 정보가 이미 존재하는지 확인
        if company_info.objects.filter(company=company).exists():
            company_already = company_info.objects.get(company=company)
            company_already.recent_employee = applicant
            if com_num == "":
                company_already.com_num = apcan_phone
            else:
                company_already.com_num = com_num
            company_already.save()
        else:
            COMPANY_NEW = company_info(
                company=company,
                com_num=com_num if com_num else apcan_phone,
                recent_employee=applicant
            )
            COMPANY_NEW.save()
        
        BOX_CREATE = apply(
            company=company,
            com_num=com_num if com_num else apcan_phone,
            applicant=applicant,
            apcan_phone=apcan_phone,
            address_num=address_num,
            address_info=address_info,
            address_detail=address_detail,
            deli_request=deli_request,
            box_num=box_num
        )
        BOX_CREATE.save()
        return redirect('apply_check')
    except Exception as e:
        # 로그를 남기거나 디버깅을 위해 예외 메시지를 출력할 수 있음
        print(f"Error: {e}")
        return redirect('failed')

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
    try:
        zir_block_kg = request.POST.get("z_b_kg")
        zir_block_count = request.POST.get("z_b_num")

        zir_powder_kg = request.POST.get("z_p_kg")
        zir_powder_count = request.POST.get("z_p_num")
        
        round_bar_kg = request.POST.get("r_b_kg")
        round_bar_count = request.POST.get("r_b_num")

        tool_kg = request.POST.get("tool_kg")
        tool_count = request.POST.get("tool_num")

        box_num = int(zir_block_count) + int(zir_powder_count) + int(round_bar_count) + int(tool_count)

        progress = 3

        company = re.sub(r'[\s]','',request.POST.get('company'))
        com_num = re.sub(r'[^0-9]','',request.POST.get('com_num'))

        applicant =re.sub(r'[\s]','',request.POST.get('applicant'))
        apcan_phone = re.sub(r'[^0-9]','',request.POST.get('apcan_phone'))
        invoice_numberaddress_num = re.sub(r'[^0-9]','',request.POST.get('invoice_num'))

        if company_info.objects.filter(company=company).exists():
            company_already = company_info.objects.get(company=company)
            company_already.recent_employee = applicant
            if com_num == "":
                company_already.com_num = apcan_phone
            else:
                company_already.com_num = com_num
            company_already.save()
        else:
            COMPANY_NEW = company_info(
                company=company,
                com_num=com_num if com_num else apcan_phone,
                recent_employee=applicant
            )
            COMPANY_NEW.save()

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
    
    except Exception as e:
        # 로그를 남기거나 디버깅을 위해 예외 메시지를 출력할 수 있음
        print(f"Error: {e}")
        return redirect('failed')

def save_failed(request):
    return render(
        request,
        'manage_apply/apply_failed.html',
    )
