# -*- coding: utf-8 -*-
from io import open


archivo= open("texto.txt","r")
texto=archivo.readlines()
with open("Output.txt", "w+", encoding="utf-8") as text_file:
    cifrado= unicode(str(text_file),errors="ignore")
mensaje=str(texto)
clave= 26
def obtenerMensajeTraducido(mensaje, clave):
     traduccion = " "
     print mensaje
     for simbolo in mensaje:
         if simbolo.isalpha():
             num = ord(simbolo)
             num += clave

             if simbolo.isupper():
                 if num > ord('Z'):
                     num -= 13
                 elif num < ord('A'):
                     num += 13
             elif simbolo.islower():
                 if num > ord('z'):
                     num -= 13
                 elif num < ord('a'):
                     num += 13

             traduccion += chr(num)
         else:
            traduccion += simbolo
     print traduccion
     traduccion= unicode(traduccion,errors="ignore")
     with open("Output.txt", "w+", encoding="utf-8") as text_file:
         text_file.write(traduccion)
     text_file.close()
     archivo.close()


def t(mensaje, clave):
    traduccion = " "
    print mensaje
    for simbolo in mensaje:
        if simbolo.isalpha():
            num = ord(simbolo)
            num -= clave

            if simbolo.isupper():
                if num > ord('Z'):
                    num += 13
                elif num < ord('A'):
                    num -= 13
            elif simbolo.islower():
                if num > ord('z'):
                    num += 13
                elif num < ord('a'):
                    num -= 13

            traduccion -= chr(num)
        else:
            traduccion -= simbolo
    print traduccion
    traduccion = unicode(traduccion, errors="ignore")
    with open("Output.txt", "w+", encoding="utf-8") as text_file:
        text_file.write(traduccion)
    text_file.close()
    archivo.close()

obtenerMensajeTraducido(mensaje,clave)