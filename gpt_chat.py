from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
chat_client = OpenAI(api_key = api_key)

# 초기 프롬프트 설정
initial_prompt = {
    "role": "user",
    "content": """You are an AI assistant that conducts simple conversations with users. Your name is 똑똑이. \n
                To answer the user's question orally, please answer in one simple sentence so that it is easy to hear.\n
                Empathize with the other person's feelings and respond as if you were a human being.\n
                Please answer in Korean."""
}

def chat_with_gpt(input_data):
    query = input_data["query"]
    chat_history = []

    chat_history.append({"role": "user", "content": query})

    response = chat_client.chat.completions.create(
        messages=chat_history,
        temperature=0.5,
        model="gpt-3.5-turbo-0613"
    )

    # AI 응답을 대화 이력에 추가
    ai_response = response.choices[0].message.content
    
    return ai_response
