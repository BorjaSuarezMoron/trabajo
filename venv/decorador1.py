def decoradora(x):
    def funcioninterior(*args):
        while True:
           yield x(*args)
    return funcioninterior
n=1
@decoradora
def suma(n):
    n=n+1
    return n
prueba = suma(n)

print next(prueba)
print next(prueba)
print next(prueba)