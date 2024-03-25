from openai import OpenAI

def openai_request(question):
    client = OpenAI()

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a genius of the web. You need to use the informations provided below to answer the question."},
        {"role": "user", "content": question}
    ]
    )

    print(completion.choices[0].message)

openai_request('como faço para enriquecer o prompt da API chat.completions com os dados de brave para ter uma resposta mais completa')
