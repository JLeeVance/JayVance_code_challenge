import pytest
from django.urls import reverse

def test_api_parse_succeeds(client):

    url = reverse('api/parse/')
    address_string = '123 main st chicago il'
    response = client.get(f'{url}?address={address_string}')

    assert response.status_code == 200
    assert 'input_string' in response.json()
    assert 'address_components' in response.json()
    assert 'address_type' in response.json()

    pytest.fail()


def test_api_parse_raises_error(client):

    url = reverse('api/parse')
    address_string = '123 main st chicago il 123 main st'
    response = client.get(f'{url}?address={address_string}')

    assert response.status_code == 400
    assert 'ErrorMessage' in response.json()
    assert 'RepeatedLabelError' in response.json()['ErrorMessage']

    pytest.fail()
