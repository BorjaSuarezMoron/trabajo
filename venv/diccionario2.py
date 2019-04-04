# -*- coding: utf-8 -*-

string_input = raw_input("Escriba ")
def prueba(string_input):

    input_list = string_input.split()  # splits the input string on spaces
    # process string elements in the list and make them integers

    print input_list
    diccionario={}
    for i in range(len(input_list)):
        valor=input_list[i]
        contador= input_list.count(valor)
        diccionario[input_list[i]]=contador
    print diccionario

prueba(string_input)
