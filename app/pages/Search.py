import streamlit as st
from models import job_criterias, get_searchterms, get_label_from_criteria, SimpleInput
from alpha import api_key, user_agent, sengdrid_key
from api import fetch_jobs_data, send_email

if 'criterias' not in st.session_state:
    st.session_state.criterias = []

if 'recipient_email' not in st.session_state:
    st.session_state.recipient_email = ''


def print_result(job_entry):
    st.write(('----------------'))
    st.markdown(
        f"[{str((job_entry['MatchedObjectDescriptor']['PositionTitle']))}]({str(job_entry['MatchedObjectDescriptor']['ApplyURI'])})")
    st.write(str(job_entry['MatchedObjectDescriptor']
             ['PositionLocation'][0]['LocationName']))
    st.write(str('Job Description: ' +
                 job_entry['MatchedObjectDescriptor']['PositionURI']))
    st.write('Salary: ' + str(job_entry['MatchedObjectDescriptor']['PositionRemuneration'][0]['MinimumRange']) + ' - ' +
             str(job_entry['MatchedObjectDescriptor']['PositionRemuneration'][0]['MaximumRange']))


def email_item_print(job_entry):
    output = ('----------------')
    output += "\n"
    output += str((job_entry['MatchedObjectDescriptor']['PositionTitle']))
    output += "\n"
    output += (str(job_entry['MatchedObjectDescriptor']
               ['PositionLocation'][0]['LocationName']))
    output += "\n"
    output += "\n"
    output += 'Application Link: ' + \
        (str(job_entry['MatchedObjectDescriptor']['ApplyURI']))
    output += "\n"
    output += "\n"
    output += (str('Job Description: ' +
                   job_entry['MatchedObjectDescriptor']['PositionURI']))
    output += "\n"
    output += "\n"
    output += ('Salary: ' + str(job_entry['MatchedObjectDescriptor']['PositionRemuneration'][0]['MinimumRange']) + ' - ' +
               str(job_entry['MatchedObjectDescriptor']['PositionRemuneration'][0]['MaximumRange']))
    return output


def email_print(jobs):
    output = ''
    for job in jobs:
        output += email_item_print(job)
        output += "\n"
        output += "\n"
        output += "\n"
    return output


st.image(
    "https://blogs.lawrence.edu/careercenter/files/2021/03/nfTYe3Ec_400x400.jpg",
    width=200)
st.markdown("# Job Search")

with st.sidebar:
    st.markdown("# Search Criteria")
    for criteria in job_criterias:
        if criteria.sidebar:
            if criteria.options is None:
                st.session_state[criteria.value] = SimpleInput(
                    st.text_input(criteria.label))
            else:
                st.session_state[criteria.value] = st.selectbox(
                    criteria.label, criteria.options, format_func=get_label_from_criteria)

for criteria in job_criterias:
    if criteria.sidebar != True:
        if criteria.options is None:
            st.session_state[criteria.value] = SimpleInput(
                st.text_input(criteria.label))
        else:
            st.session_state[criteria.value] = st.selectbox(
                criteria.label, criteria.options, format_func=get_label_from_criteria)

should_send_email = st.checkbox(
    "Would you like to receive your search results in an email?",
    value=False)
if should_send_email and st.session_state.recipient_email == "":
    st.markdown("`You need to enter your email on the home page for this feature to work.`")
if st.button("Search"):
    results = fetch_jobs_data(
        get_searchterms(
            st.session_state),
        api_key,
        user_agent)
    st.write("Please click the position title to navigate to the job application.")
    for n in results:
        print_result(n)
    if should_send_email and st.session_state.recipient_email != '':
        send_email(
            sengdrid_key,
            user_agent,
            st.session_state.recipient_email,
            email_print(results))