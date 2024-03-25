from gpt import openai_request
from brave_api_2 import brave_request

query = 'Quais sao os dias da proxima olimpiadas e onde a mesma acontecera?'
response = brave_request(query)

print(openai_request(query, ''))
print(openai_request(query, response))