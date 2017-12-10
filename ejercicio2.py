mapa = ["b.b..","b...b",".....","....b"]

def siguiente(mapaDelJuego,pocicion):

    siguiente = []

    for f in range(len(mapaDelJuego)):

        fila = []

        for c in range(len(mapaDelJuego[0])):

            fila.append(disparo(mapaDelJuego,f,c,pocicion))

        siguiente.append(fila)

    return siguiente



def disparo(mapaDelJuego,f,c,posicion):

    for x in range(len(posicion)):

        fila = (posicion[x][0])-1

        columna = (posicion[x][1])-1

        if f == fila and c == columna:

            return '.'


    return mapaDelJuego[f][c]



def posicionesDeBarcosNoHundidos(mapa, posicionesDeDisparosDePrueba):

    list = []

    for x in range(1, len(mapa)):

        if len(mapa[x - 1]) != len(mapa[x]):

            return list

    lista = []

    lista = siguiente(mapa,posicionesDeDisparosDePrueba)

    posicionesDeBarcosVivos = []

    for f in range(len(lista)):

        lista1 = ()

        for c in range(len(lista[0])):

            if lista[f][c] == 'b':

                lista1 = (f+1,c+1)

            if lista1 != [] and len(lista1) == 2:

                posicionesDeBarcosVivos.append (lista1)

                lista1 = []


    return posicionesDeBarcosVivos



posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

assert (posicionesDeBarcosNoHundidos([],posicionesDeDisparosDePrueba) == [])
assert (posicionesDeBarcosNoHundidos([""],posicionesDeDisparosDePrueba) == [])
assert (posicionesDeBarcosNoHundidos(["      "],posicionesDeDisparosDePrueba) == [])
assert (posicionesDeBarcosNoHundidos(["soy NO valido"],posicionesDeDisparosDePrueba) == [])
assert (posicionesDeBarcosNoHundidos(["yo","tambien","soy","invalido"],posicionesDeDisparosDePrueba) == [])
assert (posicionesDeBarcosNoHundidos(["b.b.","....","..bb","b.b"],posicionesDeDisparosDePrueba) == [])
assert (posicionesDeBarcosNoHundidos(["b.b..","b...b",".....","....b"],posicionesDeDisparosDePrueba) == [(2,1),(2,5)])
assert (posicionesDeBarcosNoHundidos(["b..","...","..b"],[]) == [(1,1),(3,3)])