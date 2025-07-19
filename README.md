# Mini Proyecto: Tienda de Pokemones

## Objetivo
Crear una tienda de pokemones usando Python, Poetry y las librerías `rich`, `emojise` y `requests`. El usuario podrá ver pokemones clasificados por tipo, ver detalles, agregarlos a un carrito y ver el total de su compra.

## Estructura del proyecto
```
pokemon-shop/
│
├── pyproject.toml         # Archivo de configuración de Poetry
├── README.md              # Instrucciones y documentación del proyecto
├── main.py                # Archivo resuelto (código completo)
├── activity.py            # Archivo base/documentado para que el alumno lo resuelva
└── src/
    ├── models.py          # Clases de POO: Pokemon, Categoria, Carrito, etc.
    └── utils.py           # Funciones auxiliares (peticiones, helpers, etc.)
```

## Pasos para ejecutar

1. Instala Poetry si no lo tienes:
   ```sh
   pip install poetry
   ```
2. En la carpeta del proyecto, instala las dependencias:
   ```sh
   poetry add rich emojise requests
   ```
3. Ejecuta el archivo resuelto:
   ```sh
   poetry run python main.py
   ```
4. Para resolver la actividad, edita y ejecuta `activity.py` siguiendo los comentarios.

---