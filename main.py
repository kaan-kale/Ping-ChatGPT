import openai
import time
import os
from datetime import datetime

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


def main():
    # Get the current date and time
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    result, time_taken = ask_openai("Count to 100, with a comma between each number and no newlines. E.g., 1, 2, 3, ...")

    # Write the result and date-time to the file
    with open('results.txt', 'a') as file:
        file.write(f'{date_time} - Time taken: {time_taken}\n')

    print(f"Result: {result}")

if __name__ == "__main__":
    for i in range(5):
        main()
