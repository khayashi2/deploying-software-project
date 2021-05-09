import pytest
import requests
from pytest_bdd import scenarios, when, then

FORTNITE_API = 'https://fortnite-api.com/v1/stats/br/v2'
scenarios('../feature/fortnite.feature', example_converters=dict(id=str))


@pytest.fixture
@when('the Fortnite API is queried with "<id>"')
def fort_response(id):
    params = {'format': 'json'}
    response = requests.get(FORTNITE_API + id, params=params)
    return response


@then('the response status code is 404')
def fort_response_code(fort_response):
    assert fort_response.status_code == 404

