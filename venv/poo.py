class fracciones:
    def __init__(self, dividendo, divisor):
        self.dividendo=dividendo
        self.divisor=divisor
    def __str__(self):
        cadena= str(self.dividendo)+"/"+str(self.divisor)
        return cadena

    def sumar(self, nf):
        y1 = self.divisor
        x1= self.dividendo
        y2 = nf.divisor
        x2=nf.dividendo


        xf = (x1 * y2) + (y1 * x2)
        yf= y1*y2


        f = fracciones(xf, yf)

        f.simplificar()

    def multiplicar(self, nuevafraccion):
        x1 = self.dividendo
        y1 = self.divisor
        x2 = nuevafraccion.dividendo
        y2 = nuevafraccion.divisor

        xf = x1 * x2
        yf = y1 * y2

        resultado = fracciones(xf, yf)
        print resultado
    def simplificar(self):
        x=self.dividendo
        y= self.divisor
        while (y > 0):
            resto = y
            y = x % y
            x = resto
        self.dividendo=self.dividendo//x
        self.divisor=self.divisor//x
        print self

f1=fracciones("X","Y")
f2= fracciones(2,2)
f3= fracciones(2,2)

print(f1)
f2.multiplicar(f3)
f2.sumar(f3)
f2.simplificar()

