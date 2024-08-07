from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Apply, CompanyInfo, DoneApply
import re
from .query import 이번년도_달별박스수계산, 상자_개수_추가_학습,상자_개수_예측

# Create your views here.

#요청 페이지 메인 -> 상자 or 배달 선택 페이지를 부르는 함수
def applycall(request):
    return render(
        request,
        'manage_apply/apply_page.html'
    )

#박스 배송 요청 후 신청 페이지를 부르는 함수
def box_apply_call(request):
    return render(
        request,
        "manage_apply/boxes_main.html"
    )

#신청 완료 페이지를 부르는 함수
def box_checkcall(request):
    return render(
        request,
        "manage_apply/apply_check.html"
    )


#신청 내용을 model로 저장하는 함수
def box_apply_create(request):
    try:
        ## Post.get을 통해 html에서 내용을 읽어들인 후 변수에 저장
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

        # 회사 정보가 이미 존재하는지 확인하여 있으면 정보 갱신, 없으면 회사 추가
        if CompanyInfo.objects.filter(company=company).exists():
            company_already = CompanyInfo.objects.get(company=company)
            company_already.recent_employee = applicant
            company_already.address_num = address_num
            company_already.address_info = address_info
            company_already.address_detail = address_detail
            company_already.count = int(company_already.count) + 1
            if com_num == "":
                company_already.com_num = apcan_phone
            else:
                company_already.com_num = com_num
            company_already.save()
        else:
            COMPANY_NEW = CompanyInfo(
                company=company,
                recent_employee=applicant,
                address_num=address_num,
                address_info=address_info,
                address_detail=address_detail,
                com_num=com_num if com_num else apcan_phone
            )
            COMPANY_NEW.save()

        #모델 양식에 맞게 새로운 row 만들기
        BOX_CREATE = Apply(
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
        #만든 row를 table에 추가
        BOX_CREATE.save()
        return redirect('apply_check')
    #만약 저장 실패 시, 에러 메세지를 터미널에 반환하고 에러 페이지를 띄움
    except Exception as e:
        # 로그를 남기거나 디버깅을 위해 예외 메시지를 출력할 수 있음
        print(f"Error: {e}")
        return redirect('failed')


#직접 택배로 보내는 신청페이지를 부르는 함수
def sent_page(request):
    return render(
        request,
        'manage_apply/sent_box.html',
    )

#택배로 보내는 신청페이지 내용을 model로 저장하는 함수
def sent_apply_create(request):
    try:
        ## Post.get을 통해 html에서 내용을 읽어들인 후 변수에 저장
        zir_block_count = int(request.POST.get("z_b_num",''))

        zir_powder_count = int(request.POST.get("z_p_num",''))

        round_bar_count = int(request.POST.get("r_b_num",''))

        tool_count = int(request.POST.get("tool_num",''))

        sent_box_num = zir_block_count + zir_powder_count + round_bar_count + tool_count

        progress = 2

        company = re.sub(r'[\s]','',request.POST.get('company',''))
        com_num = re.sub(r'[^0-9]','',request.POST.get('com_num',''))

        applicant =re.sub(r'[\s]','',request.POST.get('applicant',''))
        apcan_phone = re.sub(r'[^0-9]','',request.POST.get('apcan_phone',''))

        address_num = request.POST.get('sample6_postcode', '')
        address_info = request.POST.get('sample6_address', '')
        address_detail = request.POST.get('sample6_detailAddress', '')
        deli_request = request.POST.get('sample6_extraAddress', '')

        invoice_num = re.sub(r'[^0-9]','',request.POST.get('invoice_num',''))

        # 회사 정보가 이미 존재하는지 확인하여 있으면 정보 갱신, 없으면 회사 추가
        if CompanyInfo.objects.filter(company=company).exists():
            company_already = CompanyInfo.objects.get(company=company)
            company_already.recent_employee = applicant
            #우편번호가 있으면 주소 저장
            if address_num:
                company_already.address_num = address_num
                company_already.address_info = address_info
                company_already.address_detail = address_detail
                company_already.count = int(company_already.count) + 1
            if com_num == "":
                company_already.com_num = apcan_phone
            else:
                company_already.com_num = com_num
            company_already.save()
        else:
            COMPANY_NEW = CompanyInfo(
                company=company,
                recent_employee=applicant,
                address_num=address_num,
                address_info=address_info,
                address_detail=address_detail,
                com_num=com_num if com_num else apcan_phone
            )
            COMPANY_NEW.save()

        #모델 양식에 맞게 새로운 row 만들기
        SENT_CREATE = Apply(
            zir_block_count = zir_block_count,
            round_bar_count = round_bar_count,
            tool_count = tool_count,
            sent_box_num = sent_box_num,
            progress = progress,
            company = company,
            com_num = com_num,
            applicant = applicant,
            apcan_phone = apcan_phone,
            address_num=address_num,
            address_info=address_info,
            address_detail=address_detail,
            deli_request=deli_request,
            invoice_num=invoice_num,
        )
        #만든 row를 table에 추가
        SENT_CREATE.save()

        return redirect('apply_check')
    #만약 저장 실패 시, 에러 메세지를 터미널에 반환하고 에러 페이지를 띄움
    except Exception as e:
        # 로그를 남기거나 디버깅을 위해 예외 메시지를 출력할 수 있음
        print(f"Error: {e}")
        return redirect('failed')

#실패 페이지를 불러오는 함수
def save_failed(request):
    return render(
        request,
        'manage_apply/apply_failed.html',
    )

#상자 수거 요청시 조회 실패 페이지를 불러오는 함수
def pick_failed(request):
    return render(
        request,
        'manage_apply/pickreq_failed.html',
    )

#상자 수거 요청 페이지를 불러오는 함수
def research_page_call(request):
    return render(
        request,
        'manage_apply/pick_req_main.html',
    )

def research_apply(request):
    try:
        # HTML에 사용자가 입력한 값 불러오기
        company = re.sub(r'[\s]', '', request.POST.get('company', ''))
        applicant = re.sub(r'[\s]', '', request.POST.get('applicant', ''))
        apcan_phone = re.sub(r'[^0-9]', '', request.POST.get('apcan_phone', ''))

        # 불러온 값이 일치하고, 박스 배송 요청을 한 상태면 진행상황 변경 후 성공 페이지 연결
        current_apply = Apply.objects.filter(
            company=company,
            applicant=applicant,
            apcan_phone=apcan_phone,
            address_num__isnull=False,
            progress=1
        )

        if current_apply.exists():
            if current_apply.count() == 1:
                apply_instance = current_apply.first()
                apply_instance.progress = 2
                apply_instance.save()
                return redirect('request_success')
            else:
                apply_ids = list(current_apply.values_list('pk', flat=True))
                apply_ids_str = ','.join(map(str, apply_ids))
                return redirect(f'/applymain/picreq_call/?apply_ids={apply_ids_str}')
        else:
            return redirect('pick_failed')
    except Exception as e:
        # 로그를 남기거나 디버깅을 위해 예외 메시지를 출력할 수 있음
        print(f"Error in research_apply: {e}")
        return redirect('pick_failed')

def picreq_call(request):
    try:
        apply_ids_str = request.GET.get('apply_ids', '')
        apply_ids = apply_ids_str.split(',')
        applys = Apply.objects.filter(pk__in=apply_ids)
        return render(request, 'manage_apply/pic_req_list.html', {'applys': applys})
    except Exception as e:
        print(f"Error in picreq_call: {e}")
        return redirect('pick_failed')

def picreq_call_select(request):
    try:
        ids = request.POST.getlist('apply_ids')
        if ids:
            Apply.objects.filter(pk__in=ids).update(progress=2)
        return redirect('request_success')
    except Exception as e:
        print(f"Error in picreq_call_select: {e}")
        return redirect('pick_failed')


#상자 수거 요청 성공 페이지를 불러오는 함수
def req_success_call(request):
    return render(
        request,
        'manage_apply/pickreq_success.html',
    )

#진행상황전 조회 페이지를 불러오는 함수
def pro_research_call(request):
    return render(
        request,
        'manage_apply/progress_research_main.html',
    )

def pro_done_call(request):
    return render(
        request,
        'manage_apply/done_page.html',
    )

#진행상황 확인 시, 요청한 전적이 있는 지 확인하는 함수
def research_apply2(request):
    try:
        # HTML에 사용자가 입력한 값 불러오기
        company = re.sub(r'[\s]', '', request.POST.get('company', ''))
        applicant = re.sub(r'[\s]', '', request.POST.get('applicant', ''))
        apcan_phone = re.sub(r'[^0-9]', '', request.POST.get('apcan_phone', ''))

        # 불러온 값이 일치하는 신청내역 조회
        current_apply = Apply.objects.filter(
            company=company,
            applicant=applicant,
            apcan_phone=apcan_phone
        )

        if current_apply.exists():
            if current_apply.count() == 1:
                apply_id = current_apply.first().pk
                return redirect('progress_check', apply_id=apply_id)
            else:
                apply_ids = list(current_apply.values_list('pk', flat=True))
                apply_ids_str = ','.join(map(str, apply_ids))
                return redirect(f'/applymain/progress_list/?apply_ids={apply_ids_str}')
        else:
            return redirect('pick_failed')
    except Exception as e:
        # 로그를 남기거나 디버깅을 위해 예외 메시지를 출력할 수 있음
        print(f"Error: {e}")
        return redirect('pick_failed')
    
def pro_check_list(request):
    try:
        apply_ids_str = request.GET.get('apply_ids', '')
        if not apply_ids_str:
            return redirect('pick_failed')
            
        apply_ids = apply_ids_str.split(',')
        applys = Apply.objects.filter(pk__in=apply_ids)
        return render(request, 'manage_apply/progress_list.html', {'applys': applys})
    except Exception as e:
        print(f"Error in pro_check_list: {e}")
        return redirect('pick_failed')


#진행상황 페이지를 불러오는 함수
def pro_check_call(request, apply_id):
    try:
        req_apply = Apply.objects.get(pk=apply_id)
        return render(
            request,
            'manage_apply/progress_check.html',
            {'apply': req_apply}
        )
    except Apply.DoesNotExist:
        return redirect('pick_failed')


#####----아래부터 관리 페이지----#####
def manager_page_main(request):
    if request.user.is_staff:
        try:
            companys =  CompanyInfo.objects.all()
            id = request.POST.get('pk')
            return render(
                request,
                'manage_apply/manage_page.html',
                {
                    'companys':companys
                }
            )
        except Apply.DoesNotExist:
            return redirect('/')
    else:
        return redirect('/')


##박스 요청중 페이지 함수

def manage_box_req(request):
    if request.user.is_staff:
        try:
            applys = Apply.objects.filter(progress=0)
            return render(
                request,
                'manage_apply/manage_box_req.html',
                {
                    'applys': applys
                }
            )
        except Apply.DoesNotExist:
            return redirect("ma_boxreq")
    else:
        return redirect('/')

def manage_box_req_edit(request):
    if request.user.is_staff:
        try:
            # POST 요청에서 선택된 apply 객체들의 ID 목록을 가져옵니다.
            apply_ids = request.POST.getlist('apply_ids')
            if apply_ids:
                # 선택된 apply 객체들의 progress를 1로 업데이트합니다.
                Apply.objects.filter(pk__in=apply_ids).update(progress=1)
            return redirect("ma_boxreq")
        except Exception as e:
            # 예외 처리 및 디버깅 메시지
            print(f"Error: {e}")
            return redirect("ma_main")
    else:
        return redirect('/')
    
## 수거 요청중 페이지 함수
def manage_pic_req(request):
    if request.user.is_staff:
        try:
            applys = Apply.objects.filter(progress=2)
            return render(
                request,
                'manage_apply/manage_picreq.html',
                {
                    'applys': applys
                }
            )
        except Apply.DoesNotExist:
            return redirect("ma_picreq")
    else:
        return redirect('/')


def manage_pic_req_edit(request):
    if request.user.is_staff:
        try:
            # POST 요청에서 선택된 apply 객체들의 ID 목록을 가져옵니다.
            apply_ids = request.POST.getlist('apply_ids')
            if apply_ids:
                # 선택된 apply 객체들의 progress를 3으로 업데이트합니다.
                Apply.objects.filter(pk__in=apply_ids).update(progress=3)
            return redirect("ma_picreq")
        except Exception as e:
            # 예외 처리 및 디버깅 메시지
            print(f"Error: {e}")
            return redirect("ma_main")
    else:
        return redirect('/')


## 수거중 페이지 함수
def manage_pic_ing(request):
    if request.user.is_staff:
        try:
            applys = Apply.objects.filter(progress=3)
            return render(
                request,
                'manage_apply/manage_picing.html',
                {
                    'applys': applys
                }
            )
        except Apply.DoesNotExist:
            return redirect('ma_picing')
    else:
        return redirect('/')


def manage_pic_ing_edit(request):
    if request.user.is_staff:
        try:
            # POST 요청에서 선택된 apply 객체들의 ID 목록을 가져옵니다.
            apply_ids = request.POST.getlist('apply_ids')
            if apply_ids:
                # 선택된 apply 객체들을 필터링합니다.
                selected_applies = Apply.objects.filter(pk__in=apply_ids)
                
                # 각 apply 객체의 정보를 DoneApply 모델로 저장합니다.
                for apply in selected_applies:
                    Done = DoneApply(
                        company=apply.company,
                        applicant=apply.applicant,
                        apcan_phone=apply.apcan_phone,
                        box_num=apply.box_num
                    )
                    Done.save()
                    apply.delete()
            return redirect('ma_picing')
        except Exception as e:
            # 예외 처리 및 디버깅 메시지
            print(f"Error: {e}")
            return redirect("ma_main")
    else:
        return redirect('/')

#거래 끝난 것 확인 페이지
def manage_done(request):
    if request.user.is_staff:
        try:
            dones =  DoneApply.objects.all()
            id = request.POST.get('pk')
            return render(
                request,
                'manage_apply/manage_done.html',
                {
                    'dones':dones
                }
            )
        except Apply.DoesNotExist:
            return redirect('/')
    else:
        return redirect('/')


##정보 페이지 띄우기!

def 정보페이지_call(request):
    if request.user.is_staff:
        try:
            #DB 불러오기
            #만약 특정 DB만 불러오고 싶다면 Apply.objects.filter(조건)으로 불러오기
            #DB를 특정 조건으로 합쳐서 불러오고 싶다면 query.py에서 함수로 합쳐서 불러오기
            applys = Apply.objects.all()
            dones = DoneApply.objects.all()
            companys = CompanyInfo.objects.all()

            상자_개수_추가_학습()
            labels, box_nums = 이번년도_달별박스수계산()
            month_box_data = [{'label': label, 'box_num': box_num} for label, box_num in zip(labels, box_nums)]

            return render(
                request,
                'manage_apply/정보페이지.html',
                {
                    'applys': applys,
                    'dones' : dones,
                    'companys' : companys,

                    'month_box_data': month_box_data,

                }
            )
        except Apply.DoesNotExist:
            return redirect('info_call')
        except DoneApply.DoesNotExist:
            return redirect('info_call')
        except CompanyInfo.DoesNotExist:
            return redirect('info_call')
    else:
        return redirect("/")

def 상자예측_call(request):
    if request.user.is_staff:
        ym, predict = 상자_개수_예측()

        if ym is None or predict is None:
            return HttpResponse("예측 오류 발생", status=500)

        return render(
            request,
            'manage_apply/상자예측.html',
            {
                'YM': ym,
                'predict': predict,
            }
        )
    else:
        return redirect("/")