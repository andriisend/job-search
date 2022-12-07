import json
import requests
from requests.auth import HTTPBasicAuth
from app.alpha import api_key
from app.alpha import user_agent

def result(n):
    print(('----------------'))
    print(str((n['MatchedObjectDescriptor']['PositionTitle'])))
    print(str(n['MatchedObjectDescriptor']['PositionLocation'][0]['LocationName']))
    print(str('Job Description: ' + n['MatchedObjectDescriptor']['PositionURI']))
    print(str('Application Link: ' + str(n['MatchedObjectDescriptor']['ApplyURI'])))
  #if search_by == 'RemunerationMinimumAmount':
  # if float(n['MatchedObjectDescriptor']['PositionRemuneration'][0]['MinimumRange']) >= float(criteria):
    print('Salary: ' + str(n['MatchedObjectDescriptor']['PositionRemuneration'][0]['MinimumRange']) + ' - ' +
                              str(n['MatchedObjectDescriptor']['PositionRemuneration'][0]['MaximumRange']))
def send_email(n):
  client = SendGridAPIClient(sendgrid_key) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
  print("CLIENT:", type(client))
  subject = "Your USAJobs Search"
  html_content = f'Your search results: {results(n)} '
  print("HTML:", html_content)
  message = Mail(from_email=sender_email, to_emails=recipient_email, subject=subject, html_content=html_content)
  try:
    response = client.send(message)
    print("RESPONSE:", type(response)) 
    print(response.status_code) 
    print(response.body)
    print(response.headers)
  except Exception as err:
    print(type(err))
    print(err)

def results(n):
  for n in data['SearchResult']['SearchResultItems']:
    print(result(n))

criteria = ''

search_by = input("Please enter search criteria (Keyword, PositionTitle, RemunerationMinimumAmount, JobCategoryCode, Organization, PositionScheduleTypeCode) : ")
if str(search_by) == 'Organization':
  criteria = input('Please enter your organization: ')
  print(criteria)
elif str(search_by) == 'Keyword':
  criteria = input('Search by keyword: ')
elif str(search_by) == 'PositionTitle':
  criteria = input('Search by position title: ')
elif str(search_by) == 'RemunerationMinimumAmount': 
  #dropdown menu with values here
  criteria = input('Please enter minimum desired salary: ')
elif str(search_by) == 'JobCategoryCode':
  criteria = input('Please enter job category code: ')
#elif search_by == 'LocationName':
#  city = input('Please enter your city: ')
#  state = input('Please enter your state: ')
#  criteria = str(city) + ',%20' + str(state)
elif str(search_by) == 'PositionScheduleTypeCode':
  criteria = input("Please enter your schedule type code number (1 = Full-Time, 2 = Part-Time, 3 = Shift-Work, 4 = Intermittent, 5 = Job Sharing, 6 = Multiple Schedules) : ")
#    criteria = '1'
#  elif schedule_type == 'Part-Time':
#    criteria = '2'
#  elif schedule_type == 'Shift-Work':
#    criteria = '3' 
#  elif schedule_type == 'Intermittent':
#     criteria = '4'
#  elif schedule_type == 'Job Sharing':
#      criteria = '5'
#  elif schedule_type == 'Multiple Schedules':
#      criteria = '6'
my_headers = {'Host': 'data.usajobs.gov', 'User-Agent': str(user_agent),'Authorization-Key': str(api_key)}
response = requests.get(f'https://data.usajobs.gov/api/search?{search_by}={criteria}', headers=my_headers)
print(f'https://data.usajobs.gov/api/search?{search_by}={criteria}')
data = json.loads(response.text)
for n in data['SearchResult']['SearchResultItems']:
  result(n)