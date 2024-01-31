from openai import OpenAI
import time
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

def classification_and_do_process(query):
    classification_client = OpenAI()

    classification = classification_client.chat.completions.create(
        messages = [
            {
                "role": "user", 
                "content": f"""
                    Classification Task:
                    You are a classification model for a smart speaker mounted on the wall. Consider the conversation history provided above to understand the context. Your task is to categorize the following sentence into the appropriate category based on this context. The categories are as follows:
                    1. Turn on the lights, \
                    2. Turn off the lights, \
                    3. Light mode (ex: movie mode, study mode), \
                    sentence: {query}\
                    p.s your answer always must follow that 'number. categories'.
                    """
            }
        ],
        model = "gpt-4"
    )
    

    """
    1. Turn on the lights, \
    2. Turn off the lights, \
    3. Light mode (ex: movie mode, study mode), \
    """
    
    classification_content = classification.choices[0].message.content
    return classification_content


import xml.etree.ElementTree as ET
import requests
import re

# def create_xml(action, ctrl_action=None, unit_num=None):
#     imap_elem = ET.Element('imap', ver="1.0", address="192.168.100.93", sender="gpu_server93")
#     service_elem = ET.SubElement(imap_elem, "service", type="request", name="remote_access_light")
#     target_elem = ET.SubElement(service_elem, "target", name="mobile", id="1", msg_no="11")
#     action_elem = ET.SubElement(service_elem, "action")
#     action_elem.text = action

#     params = {
#         "dev_num": "1"
#     }
#     if unit_num:
#         params["unit_num"] = unit_num
#     if ctrl_action:
#         params["ctrl_action"] = ctrl_action
#     else:
#         params["uni_num"] = "null"
#         params["ctrl_action"] = "null"

#     params_elem = ET.SubElement(service_elem, "params", **params)

#     return ET.tostring(imap_elem, encoding="utf-8", method="xml")

def after_process(class_, input_text, history):
    
    payload = {
                    "query": input_text,
                    "chatHistory": history,
                }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
    }
    NEWS_SERVER_URL = 'http://192.168.100.93:5001/'
    print('분류 : ',class_)
    if class_ == "1. Turn on the lights":
        print("Turn on")
        target_url = os.path.join(NEWS_SERVER_URL, 'turn_on')
        response = requests.post(target_url, json=payload, headers=headers).json()
        return response
  
    elif class_ == "2. Turn off the lights":
        print("Turn off")
        target_url = os.path.join(NEWS_SERVER_URL, 'turn_off')
        response = requests.post(target_url, json=payload, headers=headers).json()
        return response
    
    
    elif class_ == "3. News briefing":
        target_url = os.path.join(NEWS_SERVER_URL, 'news')
        print(payload)
        response = requests.post(target_url, json=payload, headers=headers).json()
        print(response)
        return response
        # answer = response['answer']
        # audio_content = response['audioContent']

    # elif class_ == "4. Cooking menu recommendation":
    #     target_url = os.path.join(NEWS_SERVER_URL, 'recipes')
    #     response = requests.post(target_url, json=payload, headers=headers).json()
    #     return response
        answer = response['answer']
        audio_content = response['audioContent']

    elif class_ == "5. Traffic situation":
        target_url = os.path.join(NEWS_SERVER_URL, 'routes')
        response = requests.post(target_url, json=payload, headers=headers).json()
        return response
        # answer = response['answer']
        # audio_content = response['audioContent']
    
    elif class_ == "6. Light mode (ex: movie mode, study mode)":
        target_url = os.path.join(NEWS_SERVER_URL, 'light_mode')
        response = requests.post(target_url, json=payload, headers=headers).json()
        return response
    
    
    elif class_ == "8. Weather briefing":
        target_url = os.path.join(NEWS_SERVER_URL, 'weather')
        response = requests.post(target_url, json=payload, headers=headers).json()
        return response


    elif class_ == "9. Function guide":
        target_url = os.path.join(NEWS_SERVER_URL, 'function_guide')
        response = requests.post(target_url, json=payload, headers=headers).json()
        return response

    elif class_ =='10. All other categories.':
        target_url = os.path.join(NEWS_SERVER_URL, 'chat')
        response = requests.post(target_url, json=payload, headers=headers).json()
        return response
        # main_client = OpenAI(api_key = api_key)
        # # classification_content = classification.choices[0].message.content

        # assistant = main_client.beta.assistants.create(
        #     name = "Smart Speaker",
        #     instructions = "You are a Smart Speaker mounted on the wall of a house, designed to understand and formulate responses to user questions, Please check the manual and then write an answer.",
        #     tools = [{"type": "retrieval"}],
        #     # model = "gpt-3.5-turbo-1106",
        #     model  = "gpt-4-1106-preview",
        #     file_ids = ["file-9ZlrxNF5YMcYEEohIhfQdbh9"]
        # )

        # thread = main_client.beta.threads.create()

        # message = main_client.beta.threads.messages.create(
        #     thread_id = thread.id,
        #     role = "user",
        #     content = query,
        # )

        # run = main_client.beta.threads.runs.create(
        #     thread_id = thread.id,
        #     assistant_id = assistant.id,
        #     instructions="First, you should try to find an answer in the menual, but if you can't find a solution, then recommend another solution to the user. Second, do not respond in English; instead, communicate only in Korean. lastly your answer should be simple.",
        # )

        # pattern = r"【.*?】"
        # while True:
        #     run = main_client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

        #     if run.status == "completed":
        #         # print("done!")
        #         messages = main_client.beta.threads.messages.list(thread_id=thread.id)

        #         # print("messages: ")
        #         for message in messages:
        #             assert message.content[0].type == "text"
        #             # print({"role": message.role, "message": message.content[0].text.value})
        #             if message.role == "assistant":
        #                 answer = message.content[0].text.value
        #                 answer = re.sub(pattern, "", answer).replace('\n', ' ')
        #         main_client.beta.assistants.delete(assistant.id)

        #         break
        #     else:
        #         time.sleep(0.1)
        return answer
    # elif class_ == "":

