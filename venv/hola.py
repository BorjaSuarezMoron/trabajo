# -*- coding: utf-8 -*-
T="T"
trebol= [("A",T),(2,T),(3,T),(4,T),(5,T),(6,T),(7,T),(8,T),(9,T),(10,T),("J",T),("Q",T),("K",T)]
def diccionario(trebol):
    diccionario={}
    for i in range(len(trebol)):

       diccionario[trebol[i][0]]=trebol[i][1]
    print diccionario

diccionario(trebol)