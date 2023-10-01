import openai
import time

import os 

openai.api_key = os.getenv("OPENAI_API_KEY")

def calculate_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        time_taken = time.time() - start
        print(f"Time taken: {time_taken}")
        return result, time_taken
    return wrapper


@calculate_time
def ask_openai(prompt):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages,
        max_tokens=512,
        n=1,
        stop=None,
        temperature=0,
    )  
    answer = response.choices[0].message["content"]
    return answer

print(ask_openai("Count to 100, with a comma between each number and no newlines. E.g., 1, 2, 3, ..."))