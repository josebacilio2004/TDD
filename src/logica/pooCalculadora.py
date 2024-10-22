# src/calculator.py

import math

class NoSePuedeCalcular(Exception):
    """Excepción lanzada cuando no se puede calcular la media o desviación estándar."""
    pass

class CalculadoraEstadistica:
    def __init__(self):
        """
        Constructor de la clase. Inicializa una lista vacía para almacenar los elementos.
        """
        self.elementos = []

    def agregar_elemento(self, elemento):
        """
        Agrega un elemento a la lista de elementos si es numérico.
        """
        if not isinstance(elemento, (int, float)):
            raise TypeError("Solo se pueden agregar elementos numéricos.")
        self.elementos.append(elemento)

    def calcular_media(self):
        """
        Calcula la media (promedio) de los elementos. Si la lista está vacía, lanza una excepción.
        """
        if not self.elementos:
            raise NoSePuedeCalcular("La lista está vacía, no se puede calcular la media.")
        return sum(self.elementos) / len(self.elementos)

    def calcular_desviacion_estandar(self):
        """
        Calcula la desviación estándar de los elementos. Si la lista está vacía o tiene un solo
        elemento, maneja esos casos de forma adecuada.
        """
        if not self.elementos:
            raise NoSePuedeCalcular("La lista está vacía, no se puede calcular la desviación estándar.")
        if len(self.elementos) == 1:
            return 0.0  # La desviación estándar de un solo elemento es 0

        media = self.calcular_media()
        varianza = sum((x - media) ** 2 for x in self.elementos) / len(self.elementos)
        return math.sqrt(varianza)

    def limpiar_elementos(self):
        """
        Limpia todos los elementos de la lista.
        """
        self.elementos = []

    def obtener_elementos(self):
        """
        Devuelve la lista actual de elementos.
        """
        return self.elementos

if __name__ == "__main__":
    calc = CalculadoraEstadistica()

    while True:
        try:
            entrada = input("Ingresa un número (o 'fin' para terminar): ")
            if entrada.lower() == 'fin':
                break
            calc.agregar_elemento(float(entrada))
        except ValueError:
            print("Por favor, ingresa un número válido.")
        except TypeError as e:
            print(e)

    try:
        print(f"Elementos: {calc.obtener_elementos()}")
        print(f"Media: {calc.calcular_media()}")
        print(f"Desviación estándar: {calc.calcular_desviacion_estandar()}")
    except NoSePuedeCalcular as e:
        print(e)
