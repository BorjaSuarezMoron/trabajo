# -*- coding: utf-8 -*-
def recibir():
    numero=int(input("Escribe el número: "))
    while numero%2==0:
        numero= numero//2
        print numero

recibir()