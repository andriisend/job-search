import streamlit as st
from models import job_criterias, get_searchterms, get_label_from_criteria, SimpleInput
from alpha import api_key, user_agent, sengdrid_key
from PIL import Image
import os
from Home import recipient_email
from api import fetch_jobs_data, send_email

if 'criterias' not in st.session_state:
    st.session_state.criterias = []


def print_result(n):
    st.write(('----------------'))
    st.markdown(f"[{str((n['MatchedObjectDescriptor']['PositionTitle']))}]({str(n['MatchedObjectDescriptor']['ApplyURI'])})")
    st.write(str(n['MatchedObjectDescriptor']['PositionLocation'][0]['LocationName']))
    st.write(str('Job Description: ' + n['MatchedObjectDescriptor']['PositionURI']))
    st.write('Salary: ' + str(n['MatchedObjectDescriptor']['PositionRemuneration'][0]['MinimumRange']) + ' - ' +
                              str(n['MatchedObjectDescriptor']['PositionRemuneration'][0]['MaximumRange']))

def email_item_print(n):
  output = ('----------------')
  output += "\n"
  output += str((n['MatchedObjectDescriptor']['PositionTitle']))
  output += "\n"
  output +=(str(n['MatchedObjectDescriptor']['PositionLocation'][0]['LocationName']))
  output += "\n"
  output += "\n"
  output += 'Application Link: ' + (str(n['MatchedObjectDescriptor']['ApplyURI']))
  output += "\n"
  output += "\n"
  output +=(str('Job Description: ' + n['MatchedObjectDescriptor']['PositionURI']))
  output += "\n"
  output += "\n"
  output +=('Salary: ' + str(n['MatchedObjectDescriptor']['PositionRemuneration'][0]['MinimumRange']) + ' - ' +
                              str(n['MatchedObjectDescriptor']['PositionRemuneration'][0]['MaximumRange']))
  return output

def email_print(results):
  output = ''
  for n in results:
    output += email_item_print(n)
    output += "\n"
    output += "\n"
    output += "\n"
  return output


st.image("https://blogs.lawrence.edu/careercenter/files/2021/03/nfTYe3Ec_400x400.jpg", width = 200)
st.markdown("# Job Search")

with st.sidebar:
  st.markdown("# Search Criteria")
  for criteria in job_criterias:
    if criteria.sidebar:
      if criteria.options == None:
        st.session_state[criteria.value] = SimpleInput(st.text_input(criteria.label))
      else:
        st.session_state[criteria.value] = st.selectbox(criteria.label, criteria.options, format_func=get_label_from_criteria)

for criteria in job_criterias:
  if criteria.sidebar != True:
    if criteria.options == None:
      st.session_state[criteria.value] = SimpleInput(st.text_input(criteria.label))
    else:
      st.session_state[criteria.value] = st.selectbox(criteria.label, criteria.options, format_func=get_label_from_criteria)

should_send_email = st.checkbox("Would you like to receive your search results in an email?", value=False)
if st.button("Search"):
  results = fetch_jobs_data(get_searchterms(st.session_state), api_key, user_agent)
  st.write("Please click the position title to navigate to the job application.")
  for n in results:
    print_result(n)
  if should_send_email:
    send_email(sengdrid_key, user_agent, recipient_email, email_print(results))
  
