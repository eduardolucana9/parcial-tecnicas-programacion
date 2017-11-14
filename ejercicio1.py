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

def ejercicio1(palabra):

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



assert (ejercicio1("") == [])
assert (ejercicio1("     ") == [])
assert (ejercicio1("a") == ['a'])
assert (ejercicio1("ab") == ['ab','ba'])
assert (ejercicio1("paz") == ['paz','azp','zpa'])
assert (ejercicio1("so l") == ['so l','o ls',' lso','lso '])
assert (ejercicio1("rotar") == ['rotar','otarr','tarro','arrot','rrota'])
