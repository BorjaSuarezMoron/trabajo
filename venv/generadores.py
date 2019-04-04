def pares():
    n=0
    while True:
        n = n + 2

        yield n


generador=pares()

print [next(pares()) for x in xrange(2)]