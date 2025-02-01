import os
from litellm import completion
def main():
    os.environ['GOOGLE_API_KEY']='AIzaSyCAYtcMajKT_INf4a_ZXrYfjdejGJrwCsI'
messages = [{"role": "user", "content": "Hello, how are you?"}]
response = completion(model="gemini/gemini-2.0-flash-exp", messages=messages,api_key="AIzaSyCAYtcMajKT_INf4a_ZXrYfjdejGJrwCsI")
print(response)
print(response['choices'][0]['message']['content'])
print("Hello,gemini llm !")