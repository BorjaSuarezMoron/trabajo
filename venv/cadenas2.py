cadena1="Hola y adios"
cadena2="la"

def subcadenas(cadena1,cadena2):
    if cadena2 in cadena1:
        print cadena1.find(cadena2)

    else:
        print cadena2


def alfabetico(cadena1,cadena2):
    if cadena1>cadena2:
        print cadena1, cadena2
    else:
        print cadena2,cadena1

subcadenas(cadena1,cadena2)
alfabetico(cadena1,cadena2)