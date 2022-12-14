from collections import defaultdict
from app.models import Criteria, DictionaryCriteria, SimpleInput, JobCriteria, SearchInput
from app.models import get_label_from_criteria, get_searchterms

def test_criteriaequality():
    assert Criteria(
        'special',
        'speciallabel') == Criteria(
        'special',
        'speciallabel')
    assert Criteria('special1', 'special') == Criteria('special2', 'special')
    assert Criteria('special', 'special1') != Criteria('special', 'special2')


def test_dictionarycriteriaequality():
    assert DictionaryCriteria(
        'special',
        'speciallabel',
        '',
        lambda x: x) == DictionaryCriteria(
        'special',
        'speciallabel',
        '',
        lambda x: x)
    assert DictionaryCriteria(
        'special1',
        'special',
        '',
        lambda x: x) == DictionaryCriteria(
        'special2',
        'special',
        '',
        lambda x: x)
    assert DictionaryCriteria(
        'special',
        'special1',
        '',
        lambda x: x) != DictionaryCriteria(
        'special',
        'special2',
        '',
        lambda x: x)


def test_simpleinputequality():
    assert SimpleInput('special') == SimpleInput('special')
    assert SimpleInput('special') != SimpleInput('special1')


def test_jobcriteriaequality():
    assert JobCriteria(
        'special',
        'speciallabel',
        []) == JobCriteria(
        'special',
        'speciallabel',
        [])
    assert JobCriteria(
        'special1',
        'special',
        []) == JobCriteria(
        'special2',
        'special',
        [])
    assert JobCriteria(
        'special',
        'special1',
        []) != JobCriteria(
        'special',
        'special2',
        [])


def test_searchinputequality():
    assert SearchInput(None, 'special') == SearchInput(None, 'special')
    assert SearchInput(None, 'special') != SearchInput(None, 'special1')


def test_get_label_from_criteria():
    assert get_label_from_criteria(Criteria('test', 'special')) == 'test'
    assert get_label_from_criteria(None) == '-'


def test_get_searchterms():
    assert get_searchterms(defaultdict(lambda: SimpleInput(''))) == []
    storage = defaultdict(lambda: SimpleInput(''))
    storage['Keyword'] = SimpleInput('Information')
    assert get_searchterms(storage) == ['Keyword=Information']
