from flask import Flask, request, jsonify
import gpt_classification as classification
import control_function, gpt_dimming, gpt_function_guide, gpt_chat, tts
import re, time, os
os.environ["CUDA_VISIBLE_DEVICES"] = "1,2,3"

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


# 명령 분류 기능
@app.route('/classification', methods=['POST'])
def find_classification():
    start_time = time.time()
    classification_result = ''

    data = request.get_json()
    input_text = data['query']
    print('왔어?', input_text)
    try:
        # query를 분류  
        classification_result = classification.classification_and_do_process(input_text)
        
        if classification_result != None:
            match = re.match(r'\d+', classification_result)
            if match:
                category_num = int(match.group())
            return_result = {"cateCode":int(category_num)}
            
            print("결과 : ", return_result)

            # 실행 시간 계산
            end_time = time.time()
            elapsed_time = end_time - start_time
            # print(f"코드 실행 시간: {elapsed_time} 초")
            
            
            if category_num == 1: # 1. Turn on the lights
                unit_status = 'on'
                control_function.control_light(unit_status)  
                ai_response = "네! 조명을 키겠습니다."
                
            elif category_num == 2: # 2. Turn off the lights
                unit_status = 'off'
                control_function.control_light(unit_status) 
                ai_response = "네! 조명을 끄겠습니다."
                
            elif category_num == 3: # 3. Light mode (ex: movie mode, study mode)
                dimming_num = gpt_dimming.get_dimming_num(input_text)
                unit_status = 'on'
                print('dimming_num', dimming_num)
                control_function.control_light_dimming(unit_status=unit_status, dimming_num = dimming_num)
                ai_response = "조명 조절을 완료하였습니다."
            
            elif category_num == 4: # 4. Turn on the fan,
                unit_status = 'on/null/null/null/null'
                control_function.control_fan(unit_status=unit_status)
                ai_response = "팬을 켰습니다."
                
            elif category_num == 5: #5. Turn off the fan
                unit_status = 'off/null/null/null/null'
                control_function.control_fan(unit_status=unit_status)
                ai_response = "조명 조절을 완료하였습니다."

            print("채팅 결과: ", ai_response)
            response_data = {'cateCode': category_num}
            return response_data


        elif classification_result == None:
            return jsonify({'error': 'classfication 분류 실패'}), 500
    except:
        return jsonify({'error': 'classification 과정에서 문제가 발생했습니다.'}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)
    
    # host='192.168.50.180', port=8888