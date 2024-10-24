import math

import unittest
from src.logica.calculadora import CalculadoraEstadistica, NoSePuedeCalcular


class NoSePuedeCalcular(Exception):
    """Excepción lanzada cuando no se puede calcular la media o desviación estándar."""
    pass


class TestCalculadoraEstadistica(unittest.TestCase):

    def setUp(self):
        """Se ejecuta antes de cada prueba"""
        self.calc = CalculadoraEstadistica()

    def test_agregar_elemento(self):
        """Prueba para verificar que los elementos se agregan correctamente"""
        self.calc.agregar_elemento(5)
        self.assertEqual(self.calc.obtener_elementos(), [5])

        self.calc.agregar_elemento(3.5)
        self.assertEqual(self.calc.obtener_elementos(), [5, 3.5])

        with self.assertRaises(TypeError):
            self.calc.agregar_elemento("string")

    def test_calcular_media(self):
        """Prueba para la función calcular_media"""
        self.calc.agregar_elemento(10)
        self.calc.agregar_elemento(20)
        self.calc.agregar_elemento(30)
        self.assertEqual(self.calc.calcular_media(), 20)

        with self.assertRaises(NoSePuedeCalcular):
            vacia = CalculadoraEstadistica()
            vacia.calcular_media()

    def test_calcular_media_lista_vacia(self):
        calc = CalculadoraEstadistica()
        with self.assertRaises(NoSePuedeCalcular):
            calc.calcular_media()

    def test_calcular_desviacion_estandar(self):
        """Prueba para la función calcular_desviacion_estandar"""
        self.calc.agregar_elemento(10)
        self.calc.agregar_elemento(20)
        self.calc.agregar_elemento(30)
        self.assertAlmostEqual(self.calc.calcular_desviacion_estandar(), 8.1649658, places=5)

        self.calc.limpiar_elementos()  # Limpiamos para probar la excepción
        with self.assertRaises(NoSePuedeCalcular):
            self.calc.calcular_desviacion_estandar()

    def test_limpiar_elementos(self):
        """Prueba para la función limpiar_elementos"""
        self.calc.agregar_elemento(10)
        self.calc.agregar_elemento(20)
        self.calc.limpiar_elementos()
        self.assertEqual(self.calc.obtener_elementos(), [])

    def test_calcular_desviacion_estandar_un_elemento(self):
        calc = CalculadoraEstadistica()
        calc.agregar_elemento(10)
        self.assertEqual(calc.calcular_desviacion_estandar(), 0.0)

    def test_calcular_desviacion_estandar_lista_vacia(self):
        calc = CalculadoraEstadistica()
        with self.assertRaises(NoSePuedeCalcular):
            calc.calcular_desviacion_estandar()

    def test_calcular_desviacion_estandar_un_elemento(self):
        calc = CalculadoraEstadistica()
        calc.agregar_elemento(10)
        self.assertEqual(calc.calcular_desviacion_estandar(), 0.0)

    def test_obtener_elementos(self):
        """Prueba para la función obtener_elementos"""
        self.calc.agregar_elemento(10)
        self.calc.agregar_elemento(5)
        self.assertEqual(self.calc.obtener_elementos(), [10, 5])


if __name__ == "__main__":
    unittest.main()
