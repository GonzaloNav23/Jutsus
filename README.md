# Bingo de Jutsus

App de consola en Python que compara personajes de Naruto segun su elemento de chakra, usando el ciclo clásico de ventajas elementales.

## Ciclo de ventajas

```
Fuego > Viento > Rayo > Tierra > Agua > Fuego
```

## Instalacion

No necesita dependencias externas, solo Python 3.10+.

```bash
git clone <url-del-repo>
cd bingo-de-jutsus
python main.py
```

## Uso

Al ejecutar `python main.py` aparece un menu con estas opciones:

1. **Buscar personaje** - Escribe un nombre y ves sus jutsus con sus elementos.
2. **Listar todos los personajes** - Muestra todos los personajes disponibles.
3. **Comparar dos personajes** - Compara sus jutsus y dice quien tiene ventaja elemental.
4. **Salir** - Cierra la app.

## Estructura

```
bingo-de-jutsus/
├── characters.json   # Base de datos de personajes con jutsus, elementos y image_url
├── elements.py       # Logica del ciclo de ventajas elementales
├── main.py           # Interfaz de consola (menu principal)
└── README.md
```

## Imagenes

Cada personaje tiene un campo `image_url` con una URL directa y estable de la
[Naruto Fandom Wiki](https://naruto.fandom.com). En una interfaz web usa esas
URLs directamente en las etiquetas `<img>`, sin descargar los archivos:

```html
<img src="https://static.wikia.nocookie.net/naruto/images/d/d6/Naruto_Part_I.png/revision/latest?cb=20251228135525" alt="Naruto Uzumaki">
```

## Personajes incluidos

17 personajes de Konoha, Suna, Kiri, Oto, Akatsuki y Kumogakure.
