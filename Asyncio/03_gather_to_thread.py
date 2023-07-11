'''
    
    This code is written for python version 3.9

    Source: https://youtu.be/6RbJYN7SoRs

'''
import asyncio
from random import randint
from time import perf_counter

import requests

# JSON =  int | str | float | bool | None | dict[str, "JSON"] | list["JSON"]
# JSONObject = dict[str, JSON]
# JSONList = list[JSON]

def http_get_sync(url:str):
    response = requests.get(url)
    return response.json()

async def http_get(url:str):
    return await asyncio.to_thread(http_get_sync, url)

n=10

#highest pokemon id
MAX_POKEMON = 898

def get_random_pokemon_name_sync() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = http_get_sync(pokemon_url)
    return str(pokemon['name'])

async def get_random_pokemon_name() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = await http_get(pokemon_url)
    return str(pokemon['name'])

async def main() -> None:
    time_before = perf_counter()
    for _ in range(n):
        pokemon_name = get_random_pokemon_name_sync()
        print(pokemon_name)
    print(f"Time taken for sync version {perf_counter()-time_before}")
    
    time_before = perf_counter()
    result =  await asyncio.gather(*[get_random_pokemon_name() for _ in range(n)])
    print(result)
    print(f"Time taken for async version {perf_counter()-time_before}")
    
if __name__ == "__main__":
    asyncio.run(main())