from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='components/.env')

def openai_request(question,enrich):
    client = OpenAI(api_key=os.environ.get("OPENAI_API_TOKEN"),)

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a genius of the web."},
        {"role": "user", "content": question}
        {"role": "user", "content": question}
    ]
    )

    print(completion.choices[0].message)