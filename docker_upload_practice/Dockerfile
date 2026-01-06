# 1. 베이스 이미지
FROM python:3.9-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 필요한 파일을 먼저 복사 (파일이 있어야 설치가 가능함)
COPY requirements.txt .

# 4. 의존성 설치
RUN pip install -r requirements.txt

# 5. 나머지 소스 코드 복사
COPY . .

# 6. 포트 및 실행 설정
EXPOSE 5000
CMD ["python", "app.py"]