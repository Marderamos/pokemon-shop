import requests
from .models import Pokemon

def obtener_pokemones():
    url = "https://pokeapi.co/api/v2/pokemon?limit=100&offset=0"
    respuesta = requests.get(url)
    data = respuesta.json() # Dar formato JSON o Diccionario
    pokemones = []
    for poke in data["results"]:
        info = requests.get(poke["url"]).json()
        nombre = info["name"].capitalize()
        tipos = [
            t["type"]["name"].capitalize() 
            for t in info["types"]
            ]
        habilidades =[
                h["ability"]["name"] 
                for h in info["abilities"]
                ]
        peso = info["weight"]
        altura = info["height"]
        precio = peso * 10 + altura * 5
        
        pokemon = Pokemon(nombre, habilidades, peso, altura, precio, tipos)
        
        pokemones.append(pokemon)
        
    return pokemones
    
def clasificar_por_tipo(pokemones):
    categorias = {}
    for pokemon in pokemones:
        for tipo in pokemon.tipos:
            if tipo not in categorias:
                categorias[tipo] = []
            categorias[tipo].append(pokemon)
            
    return categorias