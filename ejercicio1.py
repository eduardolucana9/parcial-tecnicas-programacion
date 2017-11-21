def soloTieneEspaciosEnBlanco(palabra):

    for letra in palabra:
        if letra != " ":
            return False

    return True

def rotarPalabra(palabra):

    #PABLO => P-ABLO => ABLO-P => ABLOP

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



assert (obtenerPalabrasRotadas("     ") == [])
assert (obtenerPalabrasRotadas("a") == ['a'])
assert (obtenerPalabrasRotadas("ab") == ['ab', 'ba'])
assert (obtenerPalabrasRotadas("paz") == ['paz', 'azp', 'zpa'])
assert (obtenerPalabrasRotadas("so l") == ['so l', 'o ls', ' lso', 'lso '])
assert (obtenerPalabrasRotadas("rotar") == ['rotar', 'otarr', 'tarro', 'arrot', 'rrota'])
