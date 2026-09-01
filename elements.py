CICLO_ELEMENTAL = {
    "fuego": "viento",
    "viento": "rayo",
    "rayo": "tierra",
    "tierra": "agua",
    "agua": "fuego",
}

ELEMENTOS_VALIDOS = set(CICLO_ELEMENTAL.keys()) | {"ninguno"}


def tiene_ventaja(elemento_atacante: str, elemento_defensor: str) -> str | None:
    """Devuelve el elemento que tiene ventaja, o None si no hay ventaja directa."""
    if elemento_atacante not in ELEMENTOS_VALIDOS or elemento_defensor not in ELEMENTOS_VALIDOS:
        return None
    if elemento_atacante == "ninguno" or elemento_defensor == "ninguno":
        return None
    if CICLO_ELEMENTAL.get(elemento_atacante) == elemento_defensor:
        return elemento_atacante
    if CICLO_ELEMENTAL.get(elemento_defensor) == elemento_atacante:
        return elemento_defensor
    return None


def calcular_ventajas(jutsus_a: list[dict], jutsus_b: list[dict]) -> dict:
    """Compara las listas de jutsus de dos personajes y devuelve un resumen de ventajas."""
    elementos_a = {j["elemento"] for j in jutsus_a if j["elemento"] != "ninguno"}
    elementos_b = {j["elemento"] for j in jutsus_b if j["elemento"] != "ninguno"}

    ventajas_a = []
    ventajas_b = []

    for ea in elementos_a:
        for eb in elementos_b:
            ganador = tiene_ventaja(ea, eb)
            if ganador == ea:
                ventajas_a.append((ea, eb))
            elif ganador == eb:
                ventajas_b.append((eb, ea))

    total_a = len(ventajas_a)
    total_b = len(ventajas_b)

    if total_a > total_b:
        ganador = "A"
    elif total_b > total_a:
        ganador = "B"
    else:
        ganador = "empate"

    return {
        "elementos_a": sorted(elementos_a),
        "elementos_b": sorted(elementos_b),
        "ventajas_a": ventajas_a,
        "ventajas_b": ventajas_b,
        "puntaje_a": total_a,
        "puntaje_b": total_b,
        "ganador": ganador,
    }
