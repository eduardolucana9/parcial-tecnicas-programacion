import ejercicio1
import unittest

class TestEjercicio1(unittest.TestCase):

    def testRecibirUnaPalabraVaciaDeberiaDevolverUnaListaVacia(self):
        #ARANGE
        palabraVacia = ""

        #ACT
        resultado = ejercicio1.obtenerPalabrasRotadas(palabraVacia)

        #ASSERT
        self.assertEqual(resultado,[])


    def testRecibirUnaPalabraVaciaDeberiaDevolverUnaListaVaciaConEspacios(self):
        # ARANGE
        palabraSoloConEspaciosEnBlanco = "     "

        # ACT
        resultado = ejercicio1.obtenerPalabrasRotadas(palabraSoloConEspaciosEnBlanco)

        # ASSERT
        self.assertEqual(resultado,[])


    def testRecibirUnaPalabraDeberiaDevolverUnaListaConPalabras(self):

        palabras = "a"

        # ACT
        resultado = ejercicio1.obtenerPalabrasRotadas(palabras)

        # ASSERT
        self.assertEqual(resultado, ["a"])


    def testRecibirUnaPalabraDeberiaDevolverUnaPalabraRotada(self):

        palabras = "ab"

        resultado = ejercicio1.obtenerPalabrasRotadas(palabras)

        self.assertEqual(resultado,["ab","ba"])


    def testRecibirUnaPalabraDeberiaDevolverUnaPalabraRotada(self):

        palabra = "paz"

        resultado = ejercicio1.obtenerPalabrasRotadas(palabra)

        self.assertEqual(resultado,['paz', 'azp', 'zpa'])


    def testRecibeUnaPalabraConEspaciosDeberiaDevolverUnaPalabraRotadaConEspacios(self):

        palabraConEspacios = "so l"

        resultado = ejercicio1.obtenerPalabrasRotadas(palabraConEspacios)

        self.assertEqual(resultado,['so l', 'o ls', ' lso', 'lso '])


    def testSiRecibeUnapalabraDeberiaDevolverUnaPalabraRotada(self):

        palabra = "rotar"

        resultado = ejercicio1.obtenerPalabrasRotadas(palabra)

        self.assertEqual(resultado, ['rotar', 'otarr', 'tarro', 'arrot', 'rrota'])









