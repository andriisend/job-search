from dataclasses import dataclass
from urllib.parse import quote as urlencode


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


@dataclass
class SimpleInput:
    value: str

    def __ne__(self, other):
        if self.value == '':
            return other != '' and other is not None
        return self.value != other

    def __eq__(self, other):
        """Overrides the default implementation"""
        if str(type(other)) == str(type(self)):
            return self.value == other.value
        return False


@dataclass
class JobCriteria:
    label: str
    value: str
    options: list = None
    sidebar: bool = True

    def __eq__(self, other):
        """Overrides the default implementation"""
        if str(type(other)) == str(type(self)):
            return self.value == other.value
        return False


def get_label_from_criteria(criteria):
    if criteria is None:
        return "-"
    return criteria.label


@dataclass
class SearchInput:
    criteria: Criteria
    value: str

    def __eq__(self, other):
        """Overrides the default implementation"""
        if str(type(other)) == str(type(self)):
            return self.value == other.value and str(
                type(other.criteria)) == str(type(self.criteria))
        return False


def get_searchterms(search_input_storage):
    search_terms = []
    for criteria in job_criterias:
        if search_input_storage[criteria.value] != None:
            search_terms.append(
                f"{criteria.value}={urlencode(search_input_storage[criteria.value].value, safe=',')}")
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
    JobCriteria('Minimum Salary (e.g. 10000)', 'RemunerationMinimumAmount'),
    JobCriteria('Keyword', 'Keyword', sidebar=False),
    JobCriteria('Position Title', 'PositionTitle'),
    JobCriteria('Job Category Code', 'JobCategoryCode'),
    JobCriteria('Organization Code', 'Organization'),
    JobCriteria('Travel Preference', 'TravelPercentage', travel_requirements),
    JobCriteria(
        'Position Schedule Type',
        'PositionScheduleTypeCode',
        position_schedules),

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
    DictionaryCriteria(
        'Agency Subelements',
        'agencysubelements',
        'Please input your desired agency: ',
        agency_search),
    DictionaryCriteria(
        'Occupational Series',
        'occupationalseries',
        'Search by keyword: ',
        series_search),
    DictionaryCriteria(
        'Pay Plans',
        'payplans',
        'Search by keyword: ',
        pay_search),
    DictionaryCriteria(
        'Postal Codes',
        'postalcodes',
        'Please enter the city: ',
        postal_search)
]

# if len((data['CodeList'][0]['ValidValue'])) == 0:
#     st.write("No results found. ")
