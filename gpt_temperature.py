from openai import OpenAI
import time
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
temperature_Client = OpenAI(api_key = api_key)

def classification_and_do_process(query):
    temp_selector = temperature_Client.chat.completions.create(
                    messages = [
                        {
                            "role" : "user", 
                            "content" : f"Please provide the sentence containing the temperature. \
                                request: {args.Q} \
                                Lastly Please answer in the following format: only number of temperature, () content is omitted."
                            
                        }
                    ], 
                    model = "gpt-4"
                    # model = "gpt-3.5-turbo"
                    # model = "gpt-4-0125-preview"

                )
        
    number = temp_selector.choices[0].message.content.split(',')
    return number


