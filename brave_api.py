import os
from dotenv import load_dotenv
from brave import Brave

# Your Brave API key
load_dotenv(dotenv_path='components/.env')
api_key = os.getenv("brave_key")

brave = Brave(api_key)

query = "comment prononcer json"
num_results = 10

search_results = brave.search(q=query, count=num_results)

web_results = search_results.web_results

print(web_results)