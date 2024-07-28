from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.core.exceptions import ValidationError
import re

# Create your views here.


def blog(request):
    # 모든 post를 가져와 postlist에 저장
    postlist = Post.objects.all()
    return render(request, 'qna/blog.html', {'postlist':postlist})

def password(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
         input_password = re.sub(r'[^0-9]','',request.POST.get('password',''))
         if input_password.isdigit() and int(input_password) == post.password:
             return render(request, 'qna/posting.html', {'post': post})
         else:
             return render(request, 'qna/password_form.html', {'error': 'Incorrect password', 'post': post})
    return render(request, 'qna/password_form.html', {'post': post})

# 게시글 부르기
# def posting(request, pk):
#     post = Post.objects.get(pk=pk)
#     return render(request, 'qna/posting.html', {'post': post})


from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .models import Post
import re

def new_post(request):
    if request.method == 'POST':
        postname = request.POST.get('postname')
        contents = request.POST.get('contents')
        mainphoto = request.FILES.get('mainphoto')
        answer = request.POST.get('answer')
        password = request.POST.get('password')

        # 제목과 내용 유효성 검사
        if not postname:
            return render(request, 'qna/new_post.html', {
                'error_message': "제목을 입력해주세요"
            })

        if not contents:
            return render(request, 'qna/new_post.html', {
                'error_message': "내용을 입력해주세요"
            })
        
        # 비밀번호 유효성 검사
        if password is None or not re.match(r'^\d{4}$', password):
            return render(request, 'qna/new_post.html', {
                'error_message': "비밀번호는 숫자 4자리로 입력해주세요. (예: 1234)"
            })

        try:
            password = int(password)  # 비밀번호를 숫자로 변환
        except ValueError:
            return render(request, 'qna/new_post.html', {
                'error_message': "비밀번호는 숫자 4자리로 입력해주세요. (예: 1234)"
            })


        # 모델 인스턴스 생성
        new_post = Post(
            postname=postname,
            contents=contents,
            mainphoto=mainphoto,
            answer=answer,
            password=password,
        )

        # 모델 유효성 검사
        try:
            new_post.full_clean()  # 모든 필드와 모델 수준의 유효성 검사를 수행
        except ValidationError as e:  # 유효성 검사 실패 시 예외 처리
            return render(request, 'qna/new_post.html', {
                'error_message': e.message_dict  # 오류 메시지를 템플릿에 전달
            })

        new_post.save()  # 유효성 검사 통과 시 데이터베이스에 저장
        return redirect('qna:blog')  # 저장 후 리다이렉트

    return render(request, 'qna/new_post.html')

def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('/qna/')









