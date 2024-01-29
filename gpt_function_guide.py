from openai import OpenAI
from dotenv import load_dotenv
import os, time, re

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

def get_guide(query):
    main_client = OpenAI(api_key = api_key)

    official_file = main_client.files.create(
                                            file = open("Wallpad_Scenario.docx", "rb"),
                                            purpose = 'assistants'
                                            )
        
    official_id = official_file.id
    assistant = main_client.beta.assistants.create(
        name = "Smart Speaker",
        instructions = "You are a Smart Speaker mounted on the wall of a house, designed to understand and formulate responses to user questions, Please check the manual and then write an answer.",
        tools = [{"type": "retrieval"}],
        model  = "gpt-4-1106-preview",
        file_ids = [official_id]
    )

    thread = main_client.beta.threads.create()

    message = main_client.beta.threads.messages.create(
                                                        thread_id = thread.id,
                                                        role = "user",
                                                        content = query,
                                                    )

    run = main_client.beta.threads.runs.create(
                                                thread_id = thread.id,
                                                assistant_id = assistant.id,
                                                instructions="First, you should try to find an answer in the menual, but if you can't find a solution, then recommend another solution to the user. Second, do not respond in English; instead, communicate only in Korean. lastly your answer should be simple.",
                                            )

    pattern = r"【.*?】"
    answer = ""
    while True:
        run = main_client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

        if run.status == "completed":
            messages = main_client.beta.threads.messages.list(thread_id=thread.id)

            for message in messages:
                assert message.content[0].type == "text"
                if message.role == "assistant":
                    answer = message.content[0].text.value
                    answer = re.sub(pattern, "", answer).replace('\n', ' ')
            main_client.beta.assistants.delete(assistant.id)
            break
        else:
            time.sleep(0.1)
    return answer
