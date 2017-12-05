mapa = ["b.b..","b...b",".....","....b"]


def life_siguiente(vida,posicion):
    siguiente = []

    for i in range(len(vida)):

        fila = []

        for c in range(len(vida[0])):

            fila.append(celda_siguiente(vida,i,c,posicion))

        siguiente.append(fila)


    return siguiente

def celda_siguiente(life,f,c,posicion):

    for x in range(len(posicion)):

        fi=(posicion[x][0])-1

        co=(posicion[x][1])-1

        if f == fi and c == co:

            return '.'

    return life[f][c]


def botesHundidos(mapa,posicionesDeDisparosDePrueba):

    list = []

    for x in range(1, len(mapa)):

        if len(mapa[x - 1]) != len(mapa[x]):

            return list

    lista = []

    lista = life_siguiente(mapa,posicionesDeDisparosDePrueba)

    disparo = []

    for f in range(len(lista)):
        li = ()

        for z in range(len(lista[0])):

            if lista[f][z]== 'b':

                li = (f+1,z+1)

            if li != [] and len(li) == 2:

                disparo.append(li)
                li = []
    return disparo





def ejercicio2(var1,var2):
    return botesHundidos(var1,var2)

posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

assert (ejercicio2([],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2([""],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["      "],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["soy NO valido"],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["yo","tambien","soy","invalido"],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["b.b.","....","..bb","b.b"],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["b.b..","b...b",".....","....b"],posicionesDeDisparosDePrueba) == [(2,1),(2,5)])
assert (ejercicio2(["b..","...","..b"],[]) == [(1,1),(3,3)])