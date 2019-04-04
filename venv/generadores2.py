n=float(input("Introduce el numero: "))
def multiplos3(n):
    while True:
        yield n*3
        n = n * 3



y=multiplos3(n)
print y.next()
print y.next()
print y.next()