import streamlit as st
from models import job_criterias, get_searchterms
from alpha import api_key, user_agent, sengdrid_key
from PIL import Image
import os
import sendgrid as sg
from sendgrid.helpers.mail import Mail, Email, To, Content
from Home import recipient_email
from api import fetch_jobs_data, fetch_code_list

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

st.image("https://blogs.lawrence.edu/careercenter/files/2021/03/nfTYe3Ec_400x400.jpg", width = 200)
st.markdown("# Job Search")

with st.sidebar:
  st.markdown("# Search Criteria")
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

def email_result(n):
  for x in n:
    print_result(x)
    

if st.checkbox("Would you like to receive your search results in an email?", value=False):
  if recipient_email == None:
    st.write("Please enter your email on the Home page.")   
  else:
    sg = sg.SendGridAPIClient(sengdrid_key)
    from_email = Email(user_agent)
    to_email = To(recipient_email)  
    subject = "Your USAJobs Search"
    content = Content('text/plain', 'email_result(results)' )
    mail = Mail(from_email, to_email, subject, content)
        
    mail_json = mail.get()
      
    #response = sg.client.mail.send.post(request_body=mail_json)
    #print(response.status_code)
    #print(response.headers)
