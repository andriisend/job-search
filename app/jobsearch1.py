import streamlit as st
from dataclasses import dataclass
import requests
import json 
from requests.auth import HTTPBasicAuth
from alpha import api_key
from alpha import user_agent

def result(n):
    st.write(('----------------'))
    st.write(str((n['MatchedObjectDescriptor']['PositionTitle'])))
    st.write(str(n['MatchedObjectDescriptor']['PositionLocation'][0]['LocationName']))
    st.write(str('Job Description: ' + n['MatchedObjectDescriptor']['PositionURI']))
    st.write(str('Application Link: ' + str(n['MatchedObjectDescriptor']['ApplyURI'])))
  #if search_by == 'RemunerationMinimumAmount':
  # if float(n['MatchedObjectDescriptor']['PositionRemuneration'][0]['MinimumRange']) >= float(criteria):
    st.write('Salary: ' + str(n['MatchedObjectDescriptor']['PositionRemuneration'][0]['MinimumRange']) + ' - ' +
                              str(n['MatchedObjectDescriptor']['PositionRemuneration'][0]['MaximumRange']))
def results(n):
  for n in data['SearchResult']['SearchResultItems']:
    st.write(result(n))

def fetch_jobs_data():
    my_headers = {'Host': 'data.usajobs.gov', 'User-Agent': str(user_agent),'Authorization-Key': str(api_key)}
    response = requests.get(f'https://data.usajobs.gov/api/search?{search_by}={criteria}', headers=my_headers)
    #print(f'https://data.usajobs.gov/api/search?{search_by}={criteria}')
    data = json.loads(response.text)
    for n in data['SearchResult']['SearchResultItems']:
        result(n)


@dataclass
class Criteria:
  label: str
  value: str


def fetch_code_list(criteria):
  request_url = f"https://data.usajobs.gov/api/codelist/{dictionary_criteria.value}"
  response = requests.get(request_url)
  data = json.loads(response.text)
  return data

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

job_criteria = [
    None,
    Criteria('Position Schedule Type', 'PositionScheduleTypeCode'),
    Criteria('Minimum Salary', 'RemunerationMinimumAmount'),
    Criteria('Keyword', 'Keyword'),
    Criteria('Position Title', 'PositionTitle'),
    Criteria('Job Category Code', 'JobCategoryCode'),
]

dictionary_criteria = [
  None,
  Criteria('Agency Subelements', 'agencysubelements'),
  Criteria('Occupational Series', 'occupationalseries'),
  Criteria('Pay Plans', 'payplans'),
  Criteria('Postal Codes', 'postalcodes')
]

def get_label(criteria):
  if criteria == None:
    return "-"
  return criteria.label

st.write("Job Search")

codeList = st.selectbox(
    'Code List',
    dictionary_criteria,
    index=0,
    format_func=get_label
)

position_schedule = st.selectbox(
    'Position Schedule',
    position_schedules,
    index=0,
    format_func=get_label
)

travel_requirement = st.selectbox(
    'Travel Preferences',
    travel_requirements,
    index=0,
    format_func=get_label
)

keyword = st.text_input('Position Title')

minimum_salary = st.text_input('Minimum Salary')
#keyword_search = 'Keyword=' + keyword
#position_schedule_search = 'PositionScheduleTypeCode' + position_schedule


def search_unit():
    return 'Keyword=' + keyword
    if position_schedule != None:
        return 'PositionScheduleType=' + position_schedule



# if option != None and option1 != None and option2 != None:
#   st.write(fetch_code_list(option))
if st.button('Search', disabled=keyword==""):
  searches = []
  if codeList != None:
    searches.append(codeList.value)
  if position_schedule != None:
    searches.append(position_schedule.value)
  searches.append(keyword)
  st.write(searches)