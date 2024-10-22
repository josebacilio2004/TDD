# src/calculator.py

import math


class NoSePuedeCalcular(Exception):
    """Excepción lanzada cuando no se puede calcular la media o desviación estándar."""
    pass


def calcular_media(elementos):
    if not elementos:
        raise NoSePuedeCalcular("La lista está vacía, no se puede calcular la media.")

    if any(not isinstance(i, (int, float)) for i in elementos):
        raise TypeError("Todos los elementos deben ser numéricos.")

    return sum(elementos) / len(elementos)


def calcular_desviacion_estandar(elementos):
    if not elementos:
        raise NoSePuedeCalcular("La lista está vacía, no se puede calcular la desviación estándar.")

    if len(elementos) == 1:
        return 0.0  # La desviación estándar de un solo elemento es 0

    if any(not isinstance(i, (int, float)) for i in elementos):
        raise TypeError("Todos los elementos deben ser numéricos.")

    media = calcular_media(elementos)
    varianza = sum((x - media) ** 2 for x in elementos) / len(elementos)
    return math.sqrt(varianza)
