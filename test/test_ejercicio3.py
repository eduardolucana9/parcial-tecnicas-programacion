import ejercicio3
import unittest

class TestEjercicio3(unittest.TestCase):

    def testSiRecibeUnaListaVaciaSinEquiposDeberiaDevolverUnEquipoGanadorVacio(self):

        tuplaConEquipos = []

        resultado = ejercicio3.calcularAlEquipoGanador(tuplaConEquipos)

        self.assertEqual(resultado,"")

    def testSiRecibeUnaListaConDosEquiposDeberiaDevolverElResultadoDelEquipoGanadorConMasPuntos(self):

        tuplaConEquipos = [("a", 1, "b", 0)]

        resultado = ejercicio3.calcularAlEquipoGanador(tuplaConEquipos)

        self.assertEqual(resultado,"a")

    def testSiRecibeUnaListaConTresEquiposDeberiaDevolverElResultadoDelEquipoGanadorConMasPuntos(self):

        tuplasConEquipos = [("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]

        resultado = ejercicio3.calcularAlEquipoGanador(tuplasConEquipos)

        self.assertEqual(resultado,"c")

    def testSiRecibeUnaListaConTresEquiposDeberiaDevolverEnElCasoDeHaberEmpateDePuntosElEquipoGanadorDependeraDeOrdenAlfabetico(self):

        tuplasConEquipos = [("Boca", 1, "Belgrano", 1), ("Boca", 1, "Almagro", 1), ("Almagro", 1, "Belgrano", 1)]

        resultado = ejercicio3.calcularAlEquipoGanador(tuplasConEquipos)

        self.assertEqual(resultado,"Almagro")

    def testSiRecibeUnaListaConCuatroEquiposDeberiaDevolverElResultadoDelEquipoGanadorConMasPuntos(self):

        tuplasConEquipos = [("a", 1, "b", -2), ("a", 1, "c", 1), ("c", 1, "b", 1), ("d", 1, "a", 9)]

        resultado = ejercicio3.calcularAlEquipoGanador(tuplasConEquipos)

        self.assertEqual(resultado,"a")