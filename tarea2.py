# segundo  ejercicio
import math
import turtle
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
class Linea:
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2

    def dibujalinea(self,linea):
        linea.penup()
        linea.goto(self.p1.x*20, self.p1.y*20)
        linea.pendown()
        linea.goto(self.p2.x*20, self.p2.y*20)
        turtle.done()
    def __str__(self):
        return str(f"x: ({self.p1})")+" " +str(f"y: ({self.p2})")
class Circulo:
    def __init__(self,puntocirculo,radio):
        self.puntocirculo=puntocirculo
        self.radio=radio
    def dibujacirculo(self,circulo):
        circulo.penup()
        circulo.goto(self.puntocirculo.x*20,self.puntocirculo.y*20 - self.radio*20)
        circulo.pendown()
        circulo.circle(self.radio*20)
    def __str__(self):
        return str(f" puntos del circulo {self.puntocirculo}")+str(f"el radio del circulo {self.radio}")
punto1=Punto(2,3)
punto2=Punto(4,5)
linea=Linea(punto1,punto2)
circulo=Circulo(punto1,2)
x,y=punto1.coord_cartesianas()
r,a=punto1.coord_polares()

print("coordenadas cartesianas")
print(x,y)
print("coordenadas polares")
print(r,a)

print(punto1, "  punto 1")
print(punto2, "  punto 2")
print(linea,"  linea")

screen=turtle.Screen()
circulo_linea=turtle.Turtle()

circulo.dibujacirculo(circulo_linea)
linea.dibujalinea(circulo_linea)
turtle.done()