from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.core.exceptions import ValidationError
import re
from django.core.paginator import Paginator

# Create your views here.


def blog(request):#e
    # 모든 post를 가져와 postlist에 저장
    page = request.GET.get("page","1") #페이지 번호

    # 자주 묻는 질문/ 일반 질문 분리해서 가져오기
    faqlist = Post.objects.filter(is_faq=True).order_by('-created_at')
    postlist = Post.objects.filter(is_faq=False).order_by('-created_at')
    
    paginator = Paginator(postlist, 10) #페이지당 10개
    page_obj = paginator.get_page(page)  # 전체 데이터에서 요청한 페이지에 관한 게시글만 추출

   
    context = {
        'faqlist': faqlist,
        'postlist': page_obj
    }

    return render(request, 'qna/blog.html', context)
def password(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.is_faq:
        return render(request, 'qna/posting.html', {'post':post})
    
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
        is_faq = request.POST.get('is_faq') == 'True'
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
            is_faq = is_faq,
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
    if request.method == 'POST':
        if request.method == 'POST':
            if post.mainphoto:
                post.mainphoto.delete()
            post.delete()

        return redirect('/qna/')
    return render(request, 'qna/remove_post.html',{'Post':post})

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



import json
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


from django.shortcuts import render
from django.http import JsonResponse
from langchain.chains import RetrievalQA
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import PyPDFLoader
from langchain.chat_models import ChatOpenAI

# # 챗봇 함수
# def chatbot_response(request):
#     if request.method == 'POST':
#         user_input = request.POST.get('user_input')
        
#         print(user_input)

#         # OpenAI API 키
#         api_key = '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'  # 여기에 API 키를 입력하세요

#         # PDF 로딩 및 임베딩 준비
#         loader = PyPDFLoader('C:/newma/newma_repo/project_/chatbot.pdf')
#         documents = loader.load_and_split()

#         # OpenAIEmbeddings 객체 생성
#         embedding = OpenAIEmbeddings(openai_api_key=api_key)

#         # 벡터 데이터베이스 생성 및 리트리버 설정
#         vectordb = Chroma.from_documents(documents=documents, embedding=embedding)
#         retriever = vectordb.as_retriever(search_kwargs={'k': 1})

#         # ChatGPT 모델 설정
#         llm = ChatOpenAI(model_name='gpt-4', streaming=True, temperature=0, openai_api_key=api_key)

#         # RetrievalQA 체인 생성
#         qa_chain = RetrievalQA.from_chain_type(
#             llm=llm,
#             chain_type='stuff',
#             retriever=retriever,
#             return_source_documents=True
#         )

#         # 사용자 입력에 대한 응답 생성
#         response = qa_chain({"query": user_input})
#         print(response)
#         return JsonResponse({'result': response['result']})

#     return render(request, 'blog.html')
    
import json
import os
from django.http import JsonResponse
from django.conf import settings
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFLoader

# Chatbot 초기화 함수 (애플리케이션 시작 시 한 번만 호출)
def initialize_chatbot():
    # OpenAI API 키
    api_key = ''  # 환경 변수에서 API 키 읽기

    # PDF 로딩 및 임베딩 준비
    loader = PyPDFLoader('C:/newma/newma_repo/project_/chatbot.pdf')
    documents = loader.load_and_split()

    # OpenAIEmbeddings 객체 생성
    embedding = OpenAIEmbeddings(openai_api_key=api_key)

    # 벡터 데이터베이스 생성 및 리트리버 설정
    vectordb = Chroma.from_documents(documents=documents, embedding=embedding)
    retriever = vectordb.as_retriever(search_kwargs={'k': 1})

    # ChatGPT 모델 설정
    llm = ChatOpenAI(model_name='gpt-4', streaming=True, temperature=0, openai_api_key=api_key)

    # RetrievalQA 체인 생성
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type='stuff',
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain

# Chatbot 객체를 애플리케이션의 시작 시 한 번만 초기화
qa_chain = initialize_chatbot()

def chatbot_response(request):
    if request.method == 'POST':
        try:
            user_input = request.POST.get('user_input')
            print(user_input)
            # 사용자 입력에 대한 응답 생성
            response = qa_chain({"query": user_input})
        except:
            print(f"user_input : {user_input}")

        return JsonResponse({'result': response['result']})

    return JsonResponse({'error': 'Invalid request method'}, status=400)





def chatbot(request):
    return render(request, 'chatbot/chatbot.html')














