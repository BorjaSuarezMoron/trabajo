def decorador(x):
    def funcioninterior(*args):
        b=x(*args)
        n=pow(b,11)
        return n
    return funcioninterior

n1=1
n2=2

@decorador
def operacion(n1,n2):
    resultado=n1+n2
    return resultado

prueba=operacion(n1,n2)

print prueba