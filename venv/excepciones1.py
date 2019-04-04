# -*- coding: utf-8 -*-

def lista():
    palabra=" "
    palabras = []
    while palabra != "FIN":
        palabra = raw_input("Escribe el elemento que quieres añadir a la lista (FIN para acabar) ")
        if palabra in palabras:
         raise ValueError("Ese elemento ya se encuentra en la lista")
        else:
         palabras.append(palabra)
    print palabras
lista()