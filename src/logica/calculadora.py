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

    def calcular_media(self):
        if not self.elementos:
            raise NoSePuedeCalcular("La lista está vacía, no se puede calcular la media.")
        return sum(self.elementos) / len(self.elementos)

    def calcular_desviacion_estandar(self):
        if not self.elementos:
            raise NoSePuedeCalcular("La lista está vacía, no se puede calcular la desviación estándar.")
        if len(self.elementos) == 1:
            return 0.0  # La desviación estándar de un solo elemento es 0
        media = self.calcular_media()
        varianza = sum((x - media) ** 2 for x in self.elementos) / len(self.elementos)
        return math.sqrt(varianza)

    def limpiar_elementos(self):
        self.elementos = []

