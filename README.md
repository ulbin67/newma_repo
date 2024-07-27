# newma_repo
 뉴마 기본 서버 연결

연결 시 주의사항, setting.py는 최대한 건드리지 마세요 경로가 저장되어있습니다.
mysql 연결 하셔야합니다!


*** 모델을 건드렸는데 갑자기 사이트가 다운되었어요. OR 갑자기 서버가 안열려요. ***

모델은 DB에 연결되는 구조라 DB랑 모델 맞추기 위해 마이그레이션 해야합니다.
터미널 창에 python manage.py makemigrations
python manage.py migrate 쳐보시면 정상작동합니다!

*** DB 문제 발생시 해결 방법(수정) ***

1. 파일 안에 있는 오류 제거용 파일을 하나 복사하기
2. 실제 project_안에 있는 앱들의 파일을 오류 제거용 파일 안의 project_ 앱들의 파일로 바꿔치기 하기.(같은 이름만 바꿔치기 해주세요!)
3. mysql 스키마 삭제
4. mysql 커멘드 창에 create database newmaDB character set utf8mb4 collate utf8mb4_general_ci; 다시 입력
5. 터미널에서 project_로 들어가서 python manage.py makemigrations 터미널에 치고 문제 없는지 확인
6. 에러 있을 경우: 코드가 잘못됨, 코드에 오타나 문제 확인하세요
    에러 없을 경우: python manage.py migrate 치면 끝
