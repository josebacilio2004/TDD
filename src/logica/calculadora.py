# src/calculator.py

import math

class NoSePuedeCalcular(Exception):
    """Excepción lanzada cuando no se puede calcular la media o desviación estándar."""
    pass

class CalculadoraEstadistica:
    def __init__(self):
        self.elementos = []

    def agregar_elemento(self, elemento):
        if not isinstance(elemento, (int, float)):
            raise TypeError("Solo se pueden agregar elementos numéricos.")
        self.elementos.append(elemento)

