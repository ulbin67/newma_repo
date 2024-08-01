from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, TemplateView, FormView, UpdateView, DeleteView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from .forms import CustomUserCreationForm, CheckForm, SearchIdForm, SearchPswForm
from django.urls import reverse_lazy
from .models import User

# 메인 화면 및 로그인을 수행하는 View
def maincall(request):
    return render(request, 'single_page/main.html')


def introcall(request):
    return render(
        request,
        'single_page/introduce.html'
    )

def infocall(request):
    return render(
        request,
        'single_page/information.html'
    )

# 회원가입
class UserCreateView(CreateView):                   # 새로운 레코드 생성을 위해 CreateView 상속
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('register_done')     # 폼에 에러가 없고 테이블 생성이 완료된 경우 회원가입 성공 페이지로 이동

# 회원가입 성공시 사용
class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

# 아이디 중복체크
class UserIdCheckView(FormView):                    # 폼 검색 처리를 위해 FormView 상속
    form_class = CheckForm
    template_name = 'registration/check_id.html'

    # 아이디 중복 체크 진행 함수
    def get(self, request, *args, **kwargs):
        username = request.GET.get('username', '')              # 회원 가입시 아이디 폼에 입력된 것을 GET 방식으로 가져옴

        # 아이디 중복 체크 창에서 검색한 경우
        if args:
            username = args[0]

        # 초기 값
        is_taken = -1

        if username:
            is_taken = User.objects.filter(username=username).exists()

        return render(self.request, self.template_name, {'username': username, 'is_taken': is_taken})

    # 아이디 중복 체크 창에서 POST 발생 시 실행
    def form_valid(self, form):
        username = form.cleaned_data['check_id']
        return self.get(self.request, username)

class SearchIdView(FormView):
    template_name = 'registration/search_id.html'
    form_class = SearchIdForm

    def form_valid(self, form):
        user_name = form.cleaned_data['search_name']
        user_phone = form.cleaned_data['search_phone']
        # cer_num = form.cleaned_data['certification_num']  : 인증번호 확인 추후 추가예정

        user_info = User.objects.filter(name=user_name, phone_num=user_phone)

        if user_info.exists():
            return render(self.request, 'registration/search_id_done.html', {'user_info': user_info})
        else:
            form.add_error(None, '일치하는 정보가 없습니다. 입력을 다시 확인해 주세요.')
            return self.form_invalid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

class SearchIdDoneTV(TemplateView):
    template_name = 'registration/search_id_done.html'

class SearchPswView(FormView):
    template_name = 'registration/search_psw.html'
    form_class = SearchPswForm

    def form_valid(self, form):
        user_name = form.cleaned_data['search_name']
        user_id = form.cleaned_data['search_username']
        user_phone = form.cleaned_data['search_phone']
        # cer_num = form.cleaned_data['certification_num']  : 인증번호 확인 추후 추가예정

        user_info = User.objects.filter(name=user_name, username=user_id, phone_num=user_phone)

        if user_info.exists():
            return render(self.request, 'registration/update_passwd.html', {'user_info': user_info})
        else:
            form.add_error(None, '일치하는 정보가 없습니다. 입력을 다시 확인해 주세요.')
            return self.form_invalid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

class UpdatePswView(PasswordChangeView):
    model = User
    template_name = 'registration/update_psw.html'
    fields = ['']

class UpdatePswDoneTV(PasswordChangeDoneView):
    template_name = 'registration/update_psw_done.html'

class MyPageView(ListView):
    template_name = 'my_page/my_page.html'

class ConfirmInfoView(FormView):
    template_name = 'my_page/confirm_info.html'

class UpdateMyInfoView(UpdateView):
    template_name = 'my_page/update_info.html'

class DeleteMyInfoView(DeleteView):
    template_name = 'my_page/delete_info.html'



