# -*- coding: utf-8 -*-



archivo= open("texto.txt","r")
numero= int(input("Numero de lineas que quieres"))
def leer(archivo, numero):
    print [next(archivo) for x in range(numero)]



leer(archivo,numero)