from flask import Flask, request, jsonify
import gpt_classification as classification
import control_function, tts, gpt_light, gpt_temperature
import re, time, os, requests
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
    url = "http://192.168.170.200:80/v2/admin/sys/transfer/10.16.10.10?port=11000&secure=true"
    
    try:
        # query를 분류  
        classification_result = classification.classification_and_do_process(input_text)
        
        if classification_result != None:
            
            print("결과 : ", classification_result)
            # 실행 시간 계산
            end_time = time.time()
            elapsed_time = end_time - start_time
            
            
            if classification_result == "1. Turn on the lights":
                print("Turn on")
                target_url = url
                headers = {'Content-Type': 'application/xml'}
                control_xml = control_function.create_xml(name="remote_access_smartlight", action="control", unit_status="on")#, "switch1")
                print(control_xml)
                print()
                print(target_url)
                control_response = requests.post(target_url, data=control_xml, headers=headers, verify=False)
                print("결과", control_response)
                ai_response = str(1)
                
            elif classification_result == "2. Turn off the lights":
                print("Turn off")
                target_url = url
                headers = {'Content-Type': 'application/xml'}
                control_xml = control_function.create_xml(name="remote_access_smartlight", action="control", unit_status="off")#, "switch1")
                
                control_response = requests.post(target_url, data=control_xml, headers=headers,verify=False)
                print("이건 뭔데", control_response)
                ai_response = str(2)
                
            elif classification_result == class_ == "3. Light mode" or class_ == "3. Light mode (ex: movie mode, study mode)":
                # number = gpt_light.classification_and_do_process(input_text)
                # headers = {'Content-Type': 'application/xml'}
                # target_url = url
                # control_xml = control_function.create_xml(name = "remote_access_smartlight", action = "control", unit_status="on", unit_dimming = str(number[0]), unit_color = str(number[1]))#, "switch1")
                # control_response = requests.post(target_url, data=control_xml, headers=headers, verify=False)

                # control_xml_ = control_function.create_xml_(name = "remote_access_multivent", action="control", ctrl_action = "on/null/null/null/null")
                # control_response_ = requests.post(target_url, data=control_xml_, headers=headers, verify=False)
                ai_response = str(3)
            
            elif classification_result == "4. Turn on the gas valve":
                print("Turn on the gas valve")
                target_url = url
                headers = {'Content-Type': 'application/xml'}
                # control_xml = control_function.create_xml_other(name="remote_access_gas", action="control", ctrl_action = "close")
                # control_response = requests.post(target_url, data=control_xml, headers=headers, verify=False)
                ai_response = str(4)
                
            elif classification_result == "5. Turn off the gas valve":
                print("Turn off the gas valve")
                target_url = url
                headers = {'Content-Type': 'application/xml'}
                # control_xml = control_function.create_xml_other(name="remote_access_gas", action="control", ctrl_action = "close")
                # control_response = requests.post(target_url, data=control_xml, headers=headers, verify=False)
                ai_response = str(5)
                
            elif classification_result == "6. Turn on house heater":
                print("Turn on house heater")
                target_url = url
                headers = {'Content-Type': 'application/xml'}
                # control_xml = control_function.create_xml_other(name="remote_access_gas", action="control", ctrl_action = "close")
                # control_response = requests.post(target_url, data=control_xml, headers=headers, verify=False)
                ai_response = str(6)
                
            elif classification_result == "7. Turn off house heater":
                print("Turn off house heater")
                target_url = url
                headers = {'Content-Type': 'application/xml'}
                # control_xml = control_function.create_xml_other(name="remote_access_gas", action="control", ctrl_action = "close")
                # control_response = requests.post(target_url, data=control_xml, headers=headers, verify=False)
                ai_response = str(7)
                
            elif classification_result == "8. Set house heater target temperature":
                number = gpt_temperature.classification_and_do_process(input_text)
                # control_xml = control_function.create_xml_other(name="remote_access_gas", action="control", ctrl_action = "close")
                # control_response = requests.post(target_url, data=control_xml, headers=headers, verify=False)
                # ai_response = f"{number}도로 온도를 설정했습니다"
                ai_response = str(8)
                
            elif classification_result == "9. Turn on ventilation fan":
                print("Turn on ventilation fan")
                target_url = url
                headers = {'Content-Type': 'application/xml'}
                # control_xml = control_function.create_xml_other(name="remote_access_gas", action="control", ctrl_action = "close")
                # control_response = requests.post(target_url, data=control_xml, headers=headers, verify=False)
                ai_response = str(9)
            
            elif classification_result == "10. Turn off house heater":
                print("Turn off house heater")
                target_url = url
                headers = {'Content-Type': 'application/xml'}
                # control_xml = control_function.create_xml_other(name="remote_access_gas", action="control", ctrl_action = "close")
                # control_response = requests.post(target_url, data=control_xml, headers=headers, verify=False)
                ai_response = str(10)
                
            elif classification_result == "11. All other categories":
                print("All other categories")
                target_url = url
                headers = {'Content-Type': 'application/xml'}
                # control_xml = control_function.create_xml_other(name="remote_access_gas", action="control", ctrl_action = "close")
                # control_response = requests.post(target_url, data=control_xml, headers=headers, verify=False)
                ai_response = str(11)

            print("채팅 결과: ", ai_response)
            response_data = {'cateCode': ai_response}
            return response_data


        elif classification_result == None:
            return jsonify({'error': 'classfication 분류 실패'}), 500
    except:
            return classification_result
    # except:
    #     return jsonify({'error': 'classification 과정에서 문제가 발생했습니다.'}), 500


if __name__ == '__main__':
    app.run(debug=True, host='192.168.170.200', port=8888)
    
    # host='192.168.50.180', port=8888