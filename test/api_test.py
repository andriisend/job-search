from app.api import job_data_url, code_list_url
from app.models import SimpleInput


def test_jobs_data_url():
    assert job_data_url([]) == 'https://data.usajobs.gov/api/search?'


def test_code_list_url():
    assert code_list_url(SimpleInput('special')
                         ) == 'https://data.usajobs.gov/api/codelist/special'
