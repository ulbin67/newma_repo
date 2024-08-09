from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_community.chat_models import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


def chatbot(user_input):
    # OpenAI API 키를 직접 코드에 삽입
    api_key = ''

    # PDF 로딩 및 임베딩 준비 (초기화 시 한 번만 실행)
    loader = PyPDFLoader('C:/Users/Hong_i/Desktop/Kaggle/newma_repo/project_/chatbot.pdf')
    documents = loader.load_and_split() # pdf 파일에서 문서 내용을 로딩하고 분할

    print(documents)

    # OpenAIEmbeddings 객체 생성
    embedding = OpenAIEmbeddings(openai_api_key=api_key)

    # 벡터 데이터베이스 생성 및 리트리버 설정
    vectordb = Chroma.from_documents(documents=documents, embedding=embedding)
    result = vectordb.as_retriever(search_kwargs={'k': 1})

    # ChatGPT 모델 설정
    llm = ChatOpenAI(model_name='gpt-4o', streaming=True, temperature=0, openai_api_key=api_key)

    # RetrievalQA 체인 생성
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type='stuff',
        retriever=result,
        return_source_documents=True
        ) #QA체인을 생성해 질문 - 응답 기능을 설정
    
    print(qa_chain)

    response = qa_chain({"query": user_input})
    print( response['result'])

@csrf_exempt
def chatbot_response(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body) 
            user_input = data.get("message", "")

            # GPT-3.5 기반 답변 생성
            response = qa_chain.run(user_input) # 사용자 입력에 대해 답변 생성

            return JsonResponse({"message": response})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request method"}, status=400)

if __name__ == '__main__':
    chatbot("whai is the newma?")
    
