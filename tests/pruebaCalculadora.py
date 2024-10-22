# tests/test_calculator.py

import unittest
from src.calculator import calcular_media, calcular_desviacion_estandar, NoSePuedeCalcular


class TestCalculator(unittest.TestCase):

    def test_media_lista_vacia(self):
        with self.assertRaises(NoSePuedeCalcular):
            calcular_media([])

    def test_media_un_elemento(self):
        self.assertEqual(calcular_media([10]), 10)

    def test_media_dos_elementos(self):
        self.assertEqual(calcular_media([10, 20]), 15)

    def test_media_varios_elementos_positivos(self):
        self.assertEqual(calcular_media([10, 20, 30, 40]), 25)

    def test_media_varios_elementos_ceros(self):
        self.assertEqual(calcular_media([0, 0, 0]), 0)

    def test_media_elementos_positivos_y_negativos(self):
        self.assertEqual(calcular_media([10, -10, 20, -20]), 0)

    def test_media_elementos_no_numericos(self):
        with self.assertRaises(TypeError):
                calcular_media([10, 'a', 30])

    def test_desviacion_estandar_lista_vacia(self):
        with self.assertRaises(NoSePuedeCalcular):
                calcular_desviacion_estandar([])

    def test_desviacion_estandar_un_elemento(self):
        self.assertEqual(calcular_desviacion_estandar([10]), 0.0)

    def test_desviacion_estandar_dos_elementos(self):
        resultado = calcular_desviacion_estandar([10, 20])
        self.assertAlmostEqual(resultado, 5.0, places=2)

    def test_desviacion_estandar_varios_elementos_positivos(self):
        resultado = calcular_desviacion_estandar([10, 20, 30, 40])
        self.assertAlmostEqual(resultado, 11.18, places=2)

    def test_desviacion_estandar_varios_elementos_ceros(self):
        self.assertEqual(calcular_desviacion_estandar([0, 0, 0]), 0)

    def test_desviacion_estandar_elementos_positivos_y_negativos(self):
        resultado = calcular_desviacion_estandar([10, -10, 20, -20])
        self.assertAlmostEqual(resultado, 15.81, places=2)

    def test_desviacion_estandar_elementos_no_numericos(self):
        with self.assertRaises(TypeError):
            calcular_desviacion_estandar([10, 'a', 30])

if __name__ == "__main__":
    unittest.main()
