

import json
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


def chatbot(user_input):
    # OpenAI API 키를 직접 코드에 삽입
    api_key = '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'  # 여기에 직접 API 키를 입력합니다

    # PDF 로딩 및 임베딩 준비 (초기화 시 한 번만 실행)
    loader = PyPDFLoader('C:/Users/Hong_i/Desktop/Kaggle/newma_repo/project_/chatbot.pdf')
    documents = loader.load_and_split() # pdf 파일에서 문서 내용을 로딩하고 분할

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


    response = qa_chain({"query": user_input}) # 사용자 입력에 대해 답변 생성
    print(response['result'])


if __name__=='__main__':
    print("뉴마 담당자 전화번호 알려줘")
    chatbot("뉴마 담당자 전화번호 알려줘")