def comprobar():
    caracter= raw_input("Escriba su caracter: ")
    vocales= ["a","e","i","o","u"]
    if vocales.__contains__(caracter):
        print "Es una vocal"
    else:
        print "No es una vocal"

comprobar()