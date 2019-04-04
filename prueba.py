#!/usr/bin/python
# -*- coding: utf-8 -*-
from io import open




def getOpcion():
    while True:
        print '¿Tu quieres encriptar o desencriptar un mensaje?'
        opcion = raw_input().lower()
        if opcion in 'encriptar e desencriptar d'.split():
            return opcion
        else:
            print 'Escribir "encriptar", "e" o "desencriptar", "d".'




def encrypt(text, s, opcion):

    if opcion[0] == 'd':
        s = -s
    result = ""

    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s - ord("A")) % 26 + ord("A"))
        else:
            result += chr((ord(char) + s - ord("a")) % 26 + ord("a"))
    archivo=open("Output.txt", "w")
    archivo.write(result.decode("utf-8"))
    return result

archivo = open("texto.txt","r", encoding="utf-8")
opcion = getOpcion()
text = str(archivo.read())
s = 13

print "Plain Text : " + text
print "Shift pattern : " + str(s)
print "Cipher: " + encrypt(text, s, opcion)





