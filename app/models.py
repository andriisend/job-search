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
  def __eq__(self, other):
    """Overrides the default implementation"""
    if str(type(other)) == str(type(self)):
      return self.value == other.value
    return False

@dataclass
class DictionaryCriteria:
  label: str
  value: str
  help_text: str
  search: callable
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
    Criteria('Organization Code', 'Organization'),
    Criteria('Travel Preference', 'TravelPercentage'),
    Criteria('Location', 'LocationName')
    
]

def agency_search(search_input, data, st):
  for n in (data['CodeList'][0]['ValidValue']):
      if str(search_input) in str(n['Value']):
          st.write(str(n['Code'][0:2] + ': ' + str(n['Value'])))

def series_search(search_input, data, st):
  for n in (data['CodeList'][0]['ValidValue']):
       if str(search_input) in n['Value']:
        st.write(n['Value'])

def pay_search(search_input, data, st):
  for n in (data['CodeList'][0]['ValidValue']):
    if str(search_input) in n['Value']:
         st.write(n['Code'] + ': ' + n['Value'])

def postal_search(search_input, data, st):
  for n in (data['CodeList'][0]['ValidValue']):
        if str(search_input) in n['City']:
         st.write(n['City'] + ': ' + n['Code']) 


dictionary_criteria = [
  None,
  DictionaryCriteria('Agency Subelements', 'agencysubelements', 'Please input your desired agency: ', agency_search),
  DictionaryCriteria('Occupational Series', 'occupationalseries', 'Search by keyword: ', series_search),
  DictionaryCriteria('Pay Plans', 'payplans', 'Search by keyword: ', pay_search),
  DictionaryCriteria('Postal Codes', 'postalcodes', 'Please enter the city: ', postal_search)
]

