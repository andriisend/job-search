from dataclasses import dataclass
from alpha import sengdrid_key, user_agent
import sendgrid 
import os
from sendgrid.helpers.mail import Mail, Email, To, Content


@dataclass
class Criteria:
  label: str
  value: str
  sidebar: bool = True

def send_email():
  sg = sendgrid.SendGridAPIClient(sengdrid_key)
  from_email = Email(user_agent)  # Change to your verified sender
  to_email = To(recipient_email)  # Change to your recipient
  subject = "Your USAJobs Search"
  content = Content(content())
  mail = Mail(from_email, to_email, subject, content)#

  # Get a JSON-ready representation of the Mail object
  mail_json = mail.get()

  #Send an HTTP POST request to /mail/send
  response = sg.client.mail.send.post(request_body=mail_json)
  print(response.status_code)
  print(response.headers)

def __eq__(self, other):
    """Overrides the default implementation"""
    if str(type(other)) == str(type(self)):
      return self.value == other.value
    return False

def get_label_from_criteria(criteria):
  if criteria == None:
    return "-"
  return criteria.label

@dataclass
class SearchInput:
  criteria: Criteria
  value: str

def __eq__(self, other):
    """Overrides the default implementation"""
    if str(type(other)) == str(type(self)):
      return self.value == other.value and str(type(other.criteria)) == str(type(self.criteria))
    return False

def get_searchterms(search_input_storage):
  search_terms = []
  for criteria in job_criterias:
    if search_input_storage[criteria.value] != "":
      search_terms.append(f"{criteria.value}={search_input_storage[criteria.value]}")
  return search_terms

position_schedules = [
  None,
  Criteria('Full-Time', '1'),
  Criteria('Part-Time', '2'),
  Criteria('Shift-Work', '3'),
  Criteria('Intermittent', '4'),
  Criteria('Job Sharing', '5'),
  Criteria('Multiple Schedules', '6'),
]

travel_requirements = [
    None,
    Criteria('Not Required', '0'),
    Criteria('Occasional Travel', '1'),
    Criteria('25% or Less', '2'),
    Criteria('50% or less', '5'),
    Criteria('75% or less', '7'),
    Criteria('76% or greater', '8')
]

job_criterias = [
    Criteria('Position Schedule Type', 'PositionScheduleTypeCode'),
    Criteria('Minimum Salary', 'RemunerationMinimumAmount'),
    Criteria('Keyword', 'Keyword', False),
    Criteria('Position Title', 'PositionTitle'),
    Criteria('Job Category Code', 'JobCategoryCode'),
]