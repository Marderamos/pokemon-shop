# Vamos a crear la clase Pokemon

class Pokemon:
    def __init__(self, nombre, habilidades, peso, altura, precio, tipos):
        self.nombre = nombre
        self.habilidades = habilidades
        self.peso = peso
        self.altura = altura
        self.precio = precio
        self.tipos = tipos
        
class Carrito:
    def __init__(self):
        self.pokemones = []
        self.total = 0
        
    def agregar(self, pokemon):
        self.pokemones.append(pokemon)
        self.total += pokemon.precio
    
    def mostrar(self, console):
        from rich.table import Table  
        table = Table(title = "Carrito de pokemones", show_header=True, header_style="bold magenta")
        table.add_column("Nombre", style="bold blue")
        table.add_column("Precio", style="blue")
        for pokemon in self.pokemones:
            table.add_row(pokemon.nombre, f"${pokemon.precio}") 
        table.add_row("Total", f"${self.total}", style="bold yellow")
        console.print(table)