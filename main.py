import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'TOKEN_NAME'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
body_create = {
    "name": al000,
    "photo_id": -1
}

responseCreatePokemons = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(responseCreatePokemons.text)

pokemon_id = responseCreatePokemons.json()['id']


body_rename = {
    "pokemon_id": pokemon_id,
    "name": random_name,
    "photo_id": -1
}

responseRenamePokemons = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(responseRenamePokemons.text)

pokemon_id2 = responseRenamePokemons.json()['id']

body_catch = {
    "pokemon_id": pokemon_id2
}

responseCatchPokemons = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(responseCatchPokemons.text)