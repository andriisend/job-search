import json
import requests
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content


def job_data_url(search_terms):
    return f'https://data.usajobs.gov/api/search?{"&".join(search_terms)}'


def code_list_url(user_input):
    return f"https://data.usajobs.gov/api/codelist/{user_input.value}"


def fetch_jobs_data(search_terms, api_key, user_agent):
    my_headers = {
        'Host': 'data.usajobs.gov',
        'User-Agent': str(user_agent),
        'Authorization-Key': str(api_key)}
    response = requests.get(job_data_url(search_terms), headers=my_headers)
    return json.loads(response.text)['SearchResult']['SearchResultItems']


def fetch_code_list(user_input):
    response = requests.get(code_list_url(user_input))
    data = json.loads(response.text)
    return data


def send_email(sendgrid_key='', user_agent='', recipient_email='', body=''):
    sender = sendgrid.SendGridAPIClient(sendgrid_key)
    from_email = Email(user_agent)
    to_email = To(recipient_email)
    subject = "Your USAJobs Search"
    content = Content("text/plain", body)
    mail = Mail(from_email, to_email, subject, content)
    print(from_email)
    print(to_email)
    print(subject)
    print(content)
    mail_json = mail.get()
    response = sender.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)
