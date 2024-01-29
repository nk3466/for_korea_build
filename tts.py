from dotenv import load_dotenv
import os
import requests
import base64
from flask import jsonify

# API 요청을 위한 URL
url = "https://naveropenapi.apigw.ntruss.com/tts-premium/v1/tts"

load_dotenv()
api_id = os.getenv('CLOVA_API_KEY_ID')
api_key = os.getenv('CLOVA_API_KEY')

# 필요한 헤더 정보
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "X-NCP-APIGW-API-KEY-ID": api_id,
    "X-NCP-APIGW-API-KEY": api_key
}

def get_tts_result(input_data):
    answer = input_data['answer']

    # 데이터 설정 (목소리 종류, 텍스트, 볼륨, 속도, 피치)
    data = {
        "speaker": "vgoeun",
        "text": answer,
        "pitch": -1,
        "alpha": -1
    }

    # clova에 POST 요청 실행
    response = requests.post(url, headers=headers, data=data)
    # 응답 확인
    if response.status_code == 200:
        # 오디오 파일 내용을 Base64 인코딩으로 변환
        encoded_audio = base64.b64encode(response.content).decode()
        # 파일과 input_text를 JSON 형태로 반환
        return jsonify({
            "audioContent": encoded_audio,  # 인코딩된 오디오 파일
            "answer": answer # 입력된 텍스트,
        })
    
    else:
        print("에러:", response.status_code, response.text)
        return jsonify({'error': response.text}), 500