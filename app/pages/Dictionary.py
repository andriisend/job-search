import requests
import json 
import streamlit as st
from dataclasses import dataclass

@dataclass
class Criteria:
  label: str
  value: str
  sidebar: bool = True

dictionary_criteria = [
  None,
  Criteria('Agency Subelements', 'agencysubelements'),
  Criteria('Occupational Series', 'occupationalseries'),
  Criteria('Pay Plans', 'payplans'),
  Criteria('Postal Codes', 'postalcodes')
]

def get_label_from_criteria(Criteria):
  if Criteria == None:
    return "-"
  return Criteria.label

user_input = st.selectbox(
    'Please choose a search criteria',
    ('Agency Subelements', 'Occupational Series', 'Pay Plans', 'Postal Codes'))

#dictionary_search = get_label_from_criteria(user_input)
dictionary_search = ''
if user_input == 'Agency Subelements':
  dictionary_search = 'agencysubelements'
elif user_input == 'Occupational Series':
  dictionary_search == 'occupationalseries'
elif user_input == 'Pay Plans':
  dictionary_search == 'payplans'
elif user_input == 'Postal Codes':
  dictionary_search == 'postalcodes'

request_url = f"https://data.usajobs.gov/api/codelist/{dictionary_search}"
response = requests.get(request_url)
data = json.loads(response.text)
if dictionary_search == 'agencysubelements':
  agency_input = st.text_input("Please input your desired agency code: ")
  if st.button("Search"):
    for n in (data['CodeList'][0]['ValidValue']):
      if str(agency_input) in str(n['Code']):
          st.write(str(n['Code'][0:2] + ': ' + str(n['Value'])))
#if "ge" in user_input:
 #     user_input="agencysubelements"
 #     request_url = f"https://data.usajobs.gov/api/codelist/{user_input}"
 #     response = requests.get(request_url)
 #     data = json.loads(response.text)
 #     agency_input = input("Please input your desired agency code: ")
 ##     for n in (data['CodeList'][0]['ValidValue']):
  #     if str(agency_input) in str(n['Code']):
  #        print(str(n['Code'][0:2] + ': ' + str(n['Value'])))
#elif "ccu" in user_input:
#elif dictionary_search == 'occupationalseries':
#  if st.button("Search"):
#    for n in (data['CodeList'][0]['ValidValue']):
#      st.write(n['Value'])
elif dictionary_search == 'payplans':    
      for n in (data['CodeList'][0]['ValidValue']): 
         st.write((n['Value']))
#elif "ost" in user_input:
#      user_input="postalcodes"
#      print("Postal Codes")
#     request_url = f"https://data.usajobs.gov/api/codelist/{user_input}"
#     response = requests.get(request_url)
 #     data = json.loads(response.text)
  #    city_search = input("Please input the city: ")
  #    for n in (data['CodeList'][0]['ValidValue']):
  #      if str(city_search) in n['City']:
  #        print(n['City'] + ': ' + n['Code']) 