from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, FormView
from .forms import CustomUserCreationForm, CheckForm                    #
from django.urls import reverse_lazy
from .models import User
from django.contrib import auth
from django.contrib.auth import logout

# 메인 화면 및 로그인을 수행하는 View
def maincall(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        # 로그인 성공
        if user is not None:
            auth.login(request, user)
            return redirect('home')

        # 로그인 실패
        else:
            return redirect('register')
    else:
        return render(request, 'single_page/main.html')

# 로그아웃을 수행하는 View
def logout_view(request):
    logout(request)
    return redirect('home')

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



