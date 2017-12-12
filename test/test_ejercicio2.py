import ejercicio2
import unittest

class TestEjercicio2(unittest.TestCase):

    def testSiRecibeUnMapaVacioYConDisparosDePruebaDeberiaDevolverUnaListaVacia(self):

        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]

        mapa = []

        resultado = ejercicio2.posicionesDeBarcosNoHundidos(posicionesDeDisparosDePrueba,mapa)


        self.assertEqual(resultado,[])

    def testSirecibeUnMapaInvalidoYConDisparosDePruebaDeberiaDevolverUnaListaDePosicionesVacia(self):

        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]

        mapa = ""

        resultado = ejercicio2.posicionesDeBarcosNoHundidos(mapa,posicionesDeDisparosDePrueba)

        self.assertEqual(resultado, [])

    def testSiRecibeUnMapaInvalidoConEspaciosYConDisparosDePruebaDeberiaDevolverUnaListaDePosicionesVacia(self):

        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]

        mapa = "       "

        resultado = ejercicio2.posicionesDeBarcosNoHundidos(mapa,posicionesDeDisparosDePrueba)

        self.assertEqual(resultado, [])

    def testSiRecibeUnMapaInvalidoConPalabrasYConDisparosDePruebaDeberiaDevolverUnaListaDePosicionesVacia(self):

        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]

        mapa = "no soy valido"

        resultado = ejercicio2.posicionesDeBarcosNoHundidos(mapa,posicionesDeDisparosDePrueba)

        self.assertEqual(resultado, [])

    def testSiRecibeMapaInvalidoConVariasPalabrasYConDisparosDePruebaDeberiaDevolverUnaListaDePosicionesVacia(self):

        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]

        mapa = "yo", "tambien", "soy", "invalido"

        resultado = ejercicio2.posicionesDeBarcosNoHundidos(mapa,posicionesDeDisparosDePrueba)

        self.assertEqual(resultado, [])

    def testSirecibeUnMapaConDistintasLongitudesDeCadenasYConDisparosDePruebaDeberiaDevolverUnaListaVacia(self):

        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]

        mapa = ["b.b.", "....", "..bb", "b.b"]

        resultado = ejercicio2.posicionesDeBarcosNoHundidos(mapa,posicionesDeDisparosDePrueba)

        self.assertEqual(resultado, [])

    def testSiRecibeUnMapaValidoConDisparosDePruebaDeberiaDevolverUnaListaConLasPocicionesDeBarcosHundidosYsinHundir(self):

        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]

        mapa = ["b.b..", "b...b", ".....", "....b"]

        resultado = ejercicio2.posicionesDeBarcosNoHundidos(mapa,posicionesDeDisparosDePrueba)

        self.assertEqual(resultado, [(2, 1), (2, 5)])

    def testSiRecibeUnMapaValidoYsinDisparosDePruebaDeberiaDevolverUnaListaConLasposicionesDeBarcosHundidosYsinHundir(self):

        posicionesDeDisparosDePrueba = []

        mapa = ["b..", "...", "..b"]

        resultado = ejercicio2.posicionesDeBarcosNoHundidos(mapa,posicionesDeDisparosDePrueba)

        self.assertEqual(resultado, [(1, 1), (3, 3)])

