def soloNombresDeEquipos(tupla):
    equipos = []

    for x in range(len(tupla)):
        equipos.append(tupla[x][0])
    lista = []

    for x in sorted(set(equipos)):
        lista.append(x)

    return (lista[0])


def primerEmpaqueDeEquipos(tupla):
    lista = []

    for x in range(len(tupla)):
        listaAux = []

        for y in range(1, len(tupla[0]), 2):
            listaAux.append(tupla[x][y - 1])
            listaAux.append(tupla[x][y])

        lista.append(listaAux)

    return lista

def siSonIguales(tupla):
    lista = []
    lista = primerEmpaqueDeEquipos(tupla)
    lista = segundoEmpaque(lista)

    for x in range(1,len(lista)):

        if lista[x-1][1]==lista[x][1]:

            continue
        else:
            return False
    return True

def segundoEmpaque(lista):
    equipos = []

    for x in range(len(lista)):
        listaAux = []

        for y in range(0, len(lista[0])):
            listaAux = []

            if type(lista[x][y]) == int:
                listaAux.append(lista[x][y - 1])
                listaAux.append(lista[x][y])

            if listaAux != []:
                equipos.append(listaAux)

    return equipos

def calcularAlEquipoGanador(tupla):

    if tupla == []:

        return ""

    lista =[]
    lista = primerEmpaqueDeEquipos(tupla)
    lista=segundoEmpaque(lista)

    if siSonIguales(lista)==True:
        return soloNombresDeEquipos(lista)

    resultado = 0
    for x in range(len(lista)):

        for y in range(len(lista)):

            if lista[x][1]>lista[y][1]:
                resultado=lista[x]

    resultadoDeEquipos = resultado[0]

    return resultadoDeEquipos

