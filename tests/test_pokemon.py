import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c29c52692c104014d9ab2ecd9bba50a3'
HEADER = {'trainer_token': TOKEN}
TRAINER_ID = '7476'

def test_status_code_trainers():
    response = requests.get(url= f'{URL}/trainers')
    assert response.status_code == 200

def test_trainers_id():
    response_get = requests.get(url= f'{URL}/trainers', params= {'trainer_id': TRAINER_ID})
    assert response_get.json()['data'][0]['id'] == TRAINER_ID

@pytest.mark.parametrize('key, value', [('is_premium', True), ('id', TRAINER_ID), ('city', 'Пермь')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url= f'{URL}/trainers', params= {'trainer_id': TRAINER_ID})
    assert response_parametrize.json()['data'][0][key] == value