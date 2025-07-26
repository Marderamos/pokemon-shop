# Desde el directorio o archivo rich.console importame la clase o funcion Console 
from rich.console import Console
from rich.table import Table
# Importar toda la libreria requests y emoji
import requests
import emoji 
from src.utils import obtener_pokemones, clasificar_por_tipo
from src.models import Carrito

def mostrar_menu_categorias(categorias, console):
    console.print("\n[bold cyan]Categorías de Pokemones:[/bold cyan]")
    for i, tipo in enumerate(categorias.keys(), 1):
        console.print(f"{i}. {tipo} ")
    console.print(f"{len(categorias) +1}. Ver carrito")
    console.print(f"{len(categorias) +2}. Salir")
    return len(categorias)

def mostrar_pokemones(pokemones, console):
    table = Table(title = "Pokemones")
    table.add_column("Nombre", style = "bold magenta")
    table.add_column("Habilidades")
    table.add_column("Peso")
    table.add_column("Altura")
    table.add_column("Precio", style = "green")
    for pokemon in pokemones:
        table.add_row(
            pokemon.nombre,
            ", ".join(pokemon.habilidades),
            str(pokemon.peso),
            str(pokemon.altura),
            f"${pokemon.precio}"
        )
    console.print(table)

def main():
    console = Console()
    carrito = Carrito()
    console.print(emoji.emojize(":shopping_cart: [bold yellow] ¡Bienvenido a la tienda de pokemones.! [/bold yellow] :zap:"))
    pokemones = obtener_pokemones()
    categorias = clasificar_por_tipo(pokemones)
    
    while True: 
        n_categorias = mostrar_menu_categorias(categorias, console)
        opcion = console.input("Selecciona una opción")
        
        try:
            opcion = int(opcion)
        except ValueError: 
            console.print("[red] Por favor ingrese un número válido [/red]")        
        
        if 1 <= opcion <= n_categorias:
            tipo = list(categorias.keys())[opcion - 1]
            mostrar_pokemones(categorias[tipo], console)
            idx = input("Qué pokemon quieres comprar? (numero, enter para volver): ")
            if idx.isdigit():
                idx = int(idx)
                if 1 <= idx <= len(categorias[tipo]):
                    carrito.agregar(categorias[tipo][idx - 1])
                    console.print(emoji.emojize(":white_check_mark: [green]¡Pokemon agregado al carrito![/green]"))
        elif opcion == n_categorias + 1:
            carrito.mostrar(console)
        elif opcion == n_categorias + 2:
            console.print("[bold red]¡Gracias por tu compra![/bold red]")
            break
        else:
            console.print("[red] Opción no válida [/red]")

if __name__ == "__main__": 
    main()