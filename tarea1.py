# primero ejercicio
import math
class Punto:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def coord_cartesianas(self):
        return self.x, self.y
    def coord_polares(self):
        radio=math.sqrt(self.x*self.x+self.y*self.y)
        angulo=math.atan(self.x/self.y)
        return radio, angulo
    def __str__(self):
        return str(self.x)+" " +str(self.y)
punto1=Punto(2,3)
x,y=punto1.coord_cartesianas()
print(x,y)
r,a=punto1.coord_polares()
print(r,a)
print(punto1)