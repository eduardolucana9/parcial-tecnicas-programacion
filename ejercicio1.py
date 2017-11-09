def soloTieneEspaciosEnBlanco(palabra):

    for letra in palabra:
        if letra != " ":
            return False

    return True



def ejercicio1(palabra):

    if len(palabra) == 0:
        return []

    if soloTieneEspaciosEnBlanco(palabra):
        return []

    palabrasFinales = [palabra]

    for valor in range(len(palabra)):
        print(valor)


    return palabrasFinales





"""
assert (ejercicio1("") == [])
assert (ejercicio1("     ") == [])
assert (ejercicio1("a") == ['a'])
assert (ejercicio1("ab") == ['ab','ba'])
assert (ejercicio1("paz") == ['paz','azp','zpa'])
assert (ejercicio1("so l") == ['so l','o ls',' lso','lso '])
assert (ejercicio1("rotar") == ['rotar','otarr','tarro','arrot','rrota'])
"""

#ROTAR => R-OTAR => OTAR-R => OTARR