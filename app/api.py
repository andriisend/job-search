import requests
import json
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content

def fetch_jobs_data(search_terms, api_key, user_agent):
    my_headers = {'Host': 'data.usajobs.gov', 'User-Agent': str(user_agent),'Authorization-Key': str(api_key)}
    url = f'https://data.usajobs.gov/api/search?{"&".join(search_terms)}'
    response = requests.get(url, headers=my_headers)
    return json.loads(response.text)['SearchResult']['SearchResultItems']

def fetch_code_list(criteria):
  request_url = f"https://data.usajobs.gov/api/codelist/{dictionary_criteria.value}"
  response = requests.get(request_url)
  data = json.loads(response.text)
  return data

def send_email(sendgrid_key = '', user_agent = '', recipient_email = '', body = ''):
  sg = sendgrid.SendGridAPIClient(sendgrid_key)
  from_email = Email(user_agent)  
  to_email = To(recipient_email)  
  subject = "Your USAJobs Search"
  content = Content("text/plain", body)
  mail = Mail(from_email, to_email, subject, content)
  print(from_email)
  print(to_email)
  print(subject)
  print(content)
  
  # Get a JSON-ready representation of the Mail object
  mail_json = mail.get()

  # Send an HTTP POST request to /mail/send
  response = sg.client.mail.send.post(request_body=mail_json)
  print(response.status_code)
  print(response.headers)