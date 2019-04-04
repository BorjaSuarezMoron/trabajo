import sqlite3

conexion= sqlite3.connect("Primerabase")

cursor=conexion.cursor()

def crear():
    cursor.execute("CREATE TABLE CATEGORIAS(ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR(100) UNIQUE NOT NULL)")
    cursor.execute("CREATE TABLE CURSOS(ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR(100) UNIQUE NOT NULL, "
                   "CATEGORIA_ID INTEGER NOT NULL, FOREIGN KEY(CATEGORIA_ID) REFERENCES CATEGORIAS(ID))")


categoria="facil"
nombre="facil","baloncesto"
def insertar1(categoria):
    print categoria
    while True:
        if categoria.__contains__("facil") or categoria.__contains__("intermedio") or categoria.__contains__("avanzado"):
            resultado= cursor.execute("INSERT INTO CATEGORIAS (NOMBRE) VALUES (?)", (categoria))
            conexion.commit()
            conexion.close()
            print resultado
            False
        else:
            print("Nombre incorrecto: ")
            categoria=raw_input("Escribe otra vez la categoria: ")

def insertar2(nombre, categoria):
    x=0
    while x==0:
        if categoria == "facil":
            categoria=1
            x=1
        elif categoria == "intermedio":
            categoria=2
            x=1
        elif categoria=="avanzado":
            categoria=3
            x=1
        else:
            categoria=[raw_input("Introduzca una categoria valida: ")]
    cursor.execute("INSERT INTO CURSOS(NOMBRE,CATEGORIA_ID) VALUES (?,?)", (nombre))
    conexion.commit()
    conexion.close()

def consultar(nombre):
    resultado = cursor.execute("SELECT NOMBRE FROM CURSOS WHERE CATEGORIA_ID=(SELECT CATEGORIAS.ID FROM CATEGORIAS "
                               "WHERE CATEGORIAS.NOMBRE = ?)", nombre)
    prueba= list(resultado)
    print prueba
    conexion.close()
consultar(nombre)