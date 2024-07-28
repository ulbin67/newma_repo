from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
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


def new_post(request):
#   try:  
        if request.method == 'POST':
            postname=request.POST.get('postname')
            contents=request.POST.get('contents')
            mainphoto=request.POST.get('mainphoto')
            answer=request.POST.get('answer')
            password = int(re.sub(r'[^0-9]','',request.POST.get('password')))
            

            new_post =Post(
                postname = postname,
                contents = contents,
                mainphoto = mainphoto,
                answer = answer,
                password=password,
            )

            new_post.save()

            return redirect('qna:blog')
        return render(request, 'qna/new_post.html')
    # except:
    #     return redirect('qna:blogs')


def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('/qna/')









