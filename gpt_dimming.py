from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')


def get_dimming_num(query):
    light_client = OpenAI(api_key = api_key)
    light_selector = light_client.chat.completions.create(
                        messages = [
                            {
                                "role" : "user", 
                                "content" : f"Indicate the brightness of the light (1 to 10) and the temperature of the light (1 to 10: 1 is warm and 10 is cold) reflecting the request below as dimming: number, color: number.\
                                    request: {query} \
                                    Lastly Please answer in the following format: number of level(about dimming),number of level(about color), () content is omitted."
                                
                            }
                        ], 
                        model = "gpt-4"
                    )
    number = light_selector.choices[0].message.content.split(',')
    return number
