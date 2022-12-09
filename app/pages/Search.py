import streamlit as st
from models import job_criterias, get_searchterms, get_label_from_criteria, SimpleInput
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
    st.markdown(f"[{str((n['MatchedObjectDescriptor']['PositionTitle']))}]({str(n['MatchedObjectDescriptor']['ApplyURI'])})")
    st.write(str(n['MatchedObjectDescriptor']['PositionLocation'][0]['LocationName']))
    st.write(str('Job Description: ' + n['MatchedObjectDescriptor']['PositionURI']))
    st.write('Salary: ' + str(n['MatchedObjectDescriptor']['PositionRemuneration'][0]['MinimumRange']) + ' - ' +
                              str(n['MatchedObjectDescriptor']['PositionRemuneration'][0]['MaximumRange']))

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


if st.button("Search"):
  results = fetch_jobs_data(get_searchterms(st.session_state), api_key, user_agent)
  st.write("Please click the position title to navigate to the job application.")
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
