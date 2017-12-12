def soloTieneEspaciosEnBlanco(palabra):

    for letra in palabra:
        if letra != " ":
            return False

    return True

def rotarPalabra(palabra):


    longitudDeLaPalabra = len(palabra)
    palabraRotada = palabra[1:longitudDeLaPalabra] + palabra[0]

    return palabraRotada

def obtenerPalabrasRotadas(palabra):

    if len(palabra) == 0:
        return []

    if soloTieneEspaciosEnBlanco(palabra):
        return []

    palabrasFinales = [palabra]

    for valor in range(len(palabra)):

        if valor > 0:

            indiceDeLaUltimaPalabraRotada = len(palabrasFinales) - 1

            ultimaPalabraRotada = palabrasFinales[indiceDeLaUltimaPalabraRotada]

            palabraRotada = rotarPalabra(ultimaPalabraRotada)

            palabrasFinales.append(palabraRotada)

    return palabrasFinales



