# tests/test_calculator.py

import unittest
from src.logica.calculadora import CalculadoraEstadistica, NoSePuedeCalcular

class TestCalculadoraEstadistica(unittest.TestCase):

    def setUp(self):
        """
        Este método se ejecuta antes de cada prueba. Crea una nueva instancia
        de la clase CalculadoraEstadistica.
        """
        self.calc = CalculadoraEstadistica()

    def test_agregar_elemento_valido(self):
        """
        Prueba agregar un elemento numérico válido a la lista.
        """
        self.calc.agregar_elemento(10)
        self.assertEqual(self.calc.obtener_elementos(), [10])

    def test_agregar_elemento_no_numerico(self):
        """
        Prueba que agregar un elemento no numérico levante un TypeError.
        """
        with self.assertRaises(TypeError):
            self.calc.agregar_elemento("texto")

    def test_calcular_media_lista_vacia(self):
        """
        Prueba que calcular la media de una lista vacía levante la excepción NoSePuedeCalcular.
        """
        with self.assertRaises(NoSePuedeCalcular):
            self.calc.calcular_media()

    def test_calcular_media_un_elemento(self):
        """
        Prueba que la media de una lista con un solo elemento sea ese elemento.
        """
        self.calc.agregar_elemento(5)
        self.assertEqual(self.calc.calcular_media(), 5)

    def test_calcular_media_varios_elementos(self):
        """
        Prueba el cálculo de la media con varios elementos en la lista.
        """
        self.calc.agregar_elemento(10)
        self.calc.agregar_elemento(20)
        self.calc.agregar_elemento(30)
        self.assertEqual(self.calc.calcular_media(), 20)

    def test_calcular_desviacion_estandar_lista_vacia(self):
        """
        Prueba que calcular la desviación estándar de una lista vacía levante la excepción NoSePuedeCalcular.
        """
        with self.assertRaises(NoSePuedeCalcular):
            self.calc.calcular_desviacion_estandar()

    def test_calcular_desviacion_estandar_un_elemento(self):
        """
        Prueba que la desviación estándar de una lista con un solo elemento sea 0.
        """
        self.calc.agregar_elemento(15)
        self.assertEqual(self.calc.calcular_desviacion_estandar(), 0.0)

    def test_calcular_desviacion_estandar_varios_elementos(self):
        """
        Prueba el cálculo de la desviación estándar con varios elementos.
        """
        self.calc.agregar_elemento(10)
        self.calc.agregar_elemento(20)
        self.calc.agregar_elemento(30)
        resultado = self.calc.calcular_desviacion_estandar()
        self.assertAlmostEqual(resultado, 8.16, places=2)

    def test_limpiar_elementos(self):
        """
        Prueba que se puedan limpiar todos los elementos de la lista.
        """
        self.calc.agregar_elemento(5)
        self.calc.agregar_elemento(10)
        self.calc.limpiar_elementos()
        self.assertEqual(self.calc.obtener_elementos(), [])

if __name__ == "__main__":
    unittest.main()
