import json
from pathlib import Path

from elements import calcular_ventajas, ELEMENTOS_VALIDOS

DATA_PATH = Path(__file__).parent / "characters.json"


def cargar_personajes() -> list[dict]:
    with open(DATA_PATH, encoding="utf-8") as f:
        return json.load(f)["characters"]


def buscar_personaje(personajes: list[dict], nombre: str) -> dict | None:
    nombre_lower = nombre.lower()
    for p in personajes:
        if nombre_lower in p["nombre"].lower():
            return p
    return None


def mostrar_personaje(p: dict) -> None:
    print(f"\n{'=' * 50}")
    print(f"  {p['nombre']}")
    print(f"  Villa: {p['villa']}  |  Rango: {p['rango']}")
    print(f"{'=' * 50}")
    print("  Jutsus:")
    for j in p["jutsus"]:
        elemento = j["elemento"] if j["elemento"] != "ninguno" else "taijutsu/genjutsu"
        print(f"    - {j['nombre']}  [{elemento}]")
    print()


def comparar_personajes(personajes: list[dict]) -> None:
    nombre_a = input("Nombre del primer personaje: ").strip()
    p_a = buscar_personaje(personajes, nombre_a)
    if not p_a:
        print(f"No se encontro a '{nombre_a}'.")
        return

    nombre_b = input("Nombre del segundo personaje: ").strip()
    p_b = buscar_personaje(personajes, nombre_b)
    if not p_b:
        print(f"No se encontro a '{nombre_b}'.")
        return

    mostrar_personaje(p_a)
    mostrar_personaje(p_b)

    resultado = calcular_ventajas(p_a["jutsus"], p_b["jutsus"])

    print(f"{'=' * 50}")
    print(f"  Elementos de {p_a['nombre']}: {', '.join(resultado['elementos_a']) or 'ninguno'}")
    print(f"  Elementos de {p_b['nombre']}: {', '.join(resultado['elementos_b']) or 'ninguno'}")
    print()

    if resultado["ventajas_a"]:
        for atq, defe in resultado["ventajas_a"]:
            print(f"  {p_a['nombre']} tiene ventaja con {atq} sobre {defe} de {p_b['nombre']}")
    if resultado["ventajas_b"]:
        for atq, defe in resultado["ventajas_b"]:
            print(f"  {p_b['nombre']} tiene ventaja con {atq} sobre {defe} de {p_a['nombre']}")

    print()
    print(f"  Puntaje: {p_a['nombre']} {resultado['puntaje_a']} - {p_b['nombre']} {resultado['puntaje_b']}")

    if resultado["ganador"] == "A":
        print(f"\n  >>> {p_a['nombre']} tiene ventaja elemental <<<")
    elif resultado["ganador"] == "B":
        print(f"\n  >>> {p_b['nombre']} tiene ventaja elemental <<<")
    else:
        print("\n  >>> Empate elemental <<<")
    print()


def buscar_personaje_menu(personajes: list[dict]) -> None:
    nombre = input("Nombre del personaje: ").strip()
    p = buscar_personaje(personajes, nombre)
    if p:
        mostrar_personaje(p)
    else:
        print(f"No se encontro a '{nombre}'.")


def listar_personajes(personajes: list[dict]) -> None:
    print(f"\n{'=' * 50}")
    print("  Personajes disponibles:")
    print(f"{'=' * 50}")
    for p in sorted(personajes, key=lambda x: x["nombre"]):
        print(f"  - {p['nombre']} ({p['villa']}, {p['rango']})")
    print()


def main() -> None:
    personajes = cargar_personajes()
    print("\n=== BINGO DE JUTSUS - Naruto ===\n")

    while True:
        print("1. Buscar personaje")
        print("2. Listar todos los personajes")
        print("3. Comparar dos personajes")
        print("4. Salir")

        opcion = input("\nElige una opcion (1-4): ").strip()

        if opcion == "1":
            buscar_personaje_menu(personajes)
        elif opcion == "2":
            listar_personajes(personajes)
        elif opcion == "3":
            comparar_personajes(personajes)
        elif opcion == "4":
            print("Hasta luego, shinobi!")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
