diccionario={"Hola":"saludo", "Adios":"despedida"}
clave= raw_input("Escriba la clave que quiera buscar: ")
def superdiccionario(diccionario, clave):
    try:
        print diccionario[clave]
    except:
        print ValueError("Esta clave no existe")


superdiccionario(diccionario,clave)