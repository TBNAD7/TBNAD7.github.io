import boto3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os

# AWS Bedrock 연결을 위한 설정
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")  # 환경 변수에서 액세스 키 가져오기
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")  # 환경 변수에서 비밀 키 가져오기
region_name = "ap-northeast-2"  # Claude Sonnet 3.5 모델이 제공되는 지역

# Boto3 클라이언트 생성
client = boto3.client(
    'bedrock-runtime',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

# FastAPI 애플리케이션 생성
app = FastAPI()

# CORS 설정 (모든 도메인에서 접근 허용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인에서 접근 허용
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)

# 요청 받을 모델 정의
class QuizRequest(BaseModel):
    text: str  # 사용자가 입력한 텍스트

@app.post("/generate_quiz")
async def generate_quiz(request: QuizRequest):
    """
    Claude Sonnet 3.5 모델을 사용하여 퀴즈 문제를 생성하는 엔드포인트
    """
    try:
        # AWS Bedrock에 Claude Sonnet 3.5 모델 요청
        response = client.invoke_model(
<<<<<<< HEAD
            modelId='anthropic.claude-3-5-sonnet-20240620-v1:0',  # 모델 ID 업데이트
=======
            modelId='claude-sonnet-3.5',
>>>>>>> b853b7d (Update frontend and backend code for quiz chatbot)
            prompt=f"Generate a quiz question based on the following text: {request.text}",
            maxTokens=100
        )

        # Bedrock의 응답에서 퀴즈 질문 추출
        quiz_question = response['body'].read().decode('utf-8')

        return {"quiz_question": quiz_question}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

