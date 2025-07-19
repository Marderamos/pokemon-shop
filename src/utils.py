import requests

def obtener_pokemones():
    url = "https://pokeapi.co/api/v2/pokemon?limit=100&offset=0"
    respuesta = requests.get(url)
    data = respuesta.json()
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
        pokemones.append({
            "Nombre": nombre,
            "Tipos": tipos,
            "Habilidades": habilidades,
            "Peso": peso,
            "Altura": altura,
            "Precio": precio
            })
        return pokemones
    