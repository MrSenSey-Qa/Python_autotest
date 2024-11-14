import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c29c52692c104014d9ab2ecd9bba50a3'
HEADER = {'trainer_token': TOKEN}
body_pokemon = {
    "name": "generate",
    "photo_id": -1
}

body_update_pokemons = {
    "pokemon_id": "131960",
    "name": "generate",
    "photo_id": 123
}


response = requests.post(url = f'{URL}/pokemons', headers= HEADER, json= body_pokemon)
print(response.text)
print(response.status_code)

pokemon_id = response.json()['id']

body_pokeball = {
    "pokemon_id": pokemon_id
}

'''response_update = requests.put(url= f'{URL}/pokemons', headers= HEADER, json= body_update_pokemons)
print(response_update.text)
print(response_update.status_code)'''

response_pokeball = requests.post(url= f'{URL}/trainers/add_pokeball', headers= HEADER, json= body_pokeball)
print(response_pokeball.text)
print(response_pokeball.status_code)