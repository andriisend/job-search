import streamlit as st
from models import job_criterias, get_searchterms
from api import fetch_jobs_data
from alpha import api_key, user_agent

if 'criterias' not in st.session_state:
    st.session_state.criterias = []

def print_result(n):
    st.write(('----------------'))
    st.write(str((n['MatchedObjectDescriptor']['PositionTitle'])))
    st.write(str(n['MatchedObjectDescriptor']['PositionLocation'][0]['LocationName']))
    st.write(str('Job Description: ' + n['MatchedObjectDescriptor']['PositionURI']))
    st.write(str('Application Link: ' + str(n['MatchedObjectDescriptor']['ApplyURI'])))
  #if search_by == 'RemunerationMinimumAmount':
  # if float(n['MatchedObjectDescriptor']['PositionRemuneration'][0]['MinimumRange']) >= float(criteria):
    st.write('Salary: ' + str(n['MatchedObjectDescriptor']['PositionRemuneration'][0]['MinimumRange']) + ' - ' +
                              str(n['MatchedObjectDescriptor']['PositionRemuneration'][0]['MaximumRange']))

st.markdown("# Job Search")

with st.sidebar:
  for criteria in job_criterias:
    if criteria.sidebar:
      st.session_state[criteria.value] = st.text_input(criteria.label)

for criteria in job_criterias:
  if criteria.sidebar != True:
    st.session_state[criteria.value] = st.text_input(criteria.label)

if st.button("Search"):
  results = fetch_jobs_data(get_searchterms(st.session_state), api_key, user_agent)
  # whatever
  for n in results:
    print_result(n)