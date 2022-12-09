import requests
import json

def fetch_jobs_data(search_terms, api_key, user_agent):
    my_headers = {'Host': 'data.usajobs.gov', 'User-Agent': str(user_agent),'Authorization-Key': str(api_key)}
    url = f'https://data.usajobs.gov/api/search?{"&".join(search_terms)}'
    print(url)
    response = requests.get(url, headers=my_headers)
    return json.loads(response.text)['SearchResult']['SearchResultItems']

def fetch_code_list(criteria):
  request_url = f"https://data.usajobs.gov/api/codelist/{dictionary_criteria.value}"
  response = requests.get(request_url)
  data = json.loads(response.text)
  return data

