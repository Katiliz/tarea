import unittest

def suma(nro1, nro2):
    return nro1 + nro2

def resta(nro1, nro2):
    return nro1 - nro2

def multiplicacion(nro1, nro2):
    return nro1 * nro2

def division(nro1, nro2):
    if nro2 == 0:
        raise ValueError("No se puede dividir entre cero")
    return nro1 / nro2

def MCDbasic(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def MCDcompuesto(n1, n2, n3, n4):
    mcd1 = MCDbasic(n1, n2)
    mcd2 = MCDbasic(mcd1, n3)
    return MCDbasic(mcd2, n4)

class TestOperaciones(unittest.TestCase):
    def test_suma(self):
        esperado = 20
        actual = suma(5, 15)
        self.assertEqual(actual, esperado)

    def test_resta(self):
        esperado = 5
        actual = resta(15, 10)
        self.assertEqual(actual, esperado)

    def test_multiplicacion(self):
        esperado = 20
        actual = multiplicacion(4, 5)
        self.assertEqual(actual, esperado)

    def test_division(self):
        esperado = 5
        actual = division(20, 4)
        self.assertEqual(actual, esperado)

    def test_MCDbasic(self):
        esperado = 2
        actual = MCDbasic(10, 12)
        self.assertEqual(actual, esperado)

    def test_MCDcompuesto(self):
        esperado = 2
        actual = MCDcompuesto(20, 6, 8, 14)
        self.assertEqual(actual, esperado)

if __name__ == '__main__':
    unittest.main()




