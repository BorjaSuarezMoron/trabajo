from random import randrange
D= "D"
T="T"
P="P"
C="C"
diamante= (1,D),(2,D),(3,D),(4,D),(5,D),(6,D),(7,D),(8,D),(9,D),(10,D),(11,D),(12,D),(13,D)
corazon= (1,C),(2,C),(3,C),(4,C),(5,C),(6,C),(7,C),(8,C),(9,C),(10,C),(11,C),(12,C),(13,C)
pica= (1,P),(2,P),(3,P),(4,P),(5,P),(6,P),(7,P),(8,P),(9,P),(10,P),(11,P),(12,P),(13,P)
trebol= (1,T),(2,T),(3,T),(4,T),(5,T),(6,T),(7,T),(8,T),(9,T),(10,T),(11,T),(12,T),(13,T)
baraja = diamante, trebol, pica, corazon

def valor(x):
    return x[0]
def aleatorio(baraja):
    mano= []
    for i in range(0,5):
        carta= baraja[randrange(0,4)][randrange (0,12)]
        mano.append(carta)
    mano1= map(valor, mano)
    prueba= set(mano1)
    print prueba
    if len(prueba)<3:
        print "Poker"
    else:
        print "No poker"


aleatorio(baraja)