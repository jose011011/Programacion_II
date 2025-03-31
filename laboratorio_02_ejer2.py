import math

class Algebra_Lineal:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y  
        self.z = z

    def suma(self, other):
        return Algebra_Lineal(self.x + other.x, self.y + other.y, self.z + other.z)

    def resta(self, other):
        return Algebra_Lineal(self.x - other.x, self.y - other.y, self.z - other.z)

    def producto_cruz(self, other):
        return Algebra_Lineal(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def es_perpendicular(self, other):
        return (self.x * other.x + self.y * other.y + self.z * other.z) == 0

    def es_paralelo(self, other):
        pc = self.producto_cruz(other)
        return pc.x == 0 and pc.y == 0 and pc.z == 0

    def proyeccion_sobre(self, other):
        dot = self.x * other.x + self.y * other.y + self.z * other.z
        mag2 = other.magnitud() ** 2
        factor = dot / mag2
        return Algebra_Lineal(factor * other.x, factor * other.y, factor * other.z)

    def componente_en(self, other):
        dot = self.x * other.x + self.y * other.y + self.z * other.z
        return dot / other.magnitud()

    def __add__(self, other):
        return self.suma(other)

    def __sub__(self, other):
        return self.resta(other)

    def __mul__(self, other):
        if isinstance(other, Algebra_Lineal):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise TypeError("El operador * solo se usa para producto punto con otro vector.")

    def __xor__(self, other):
        return self.producto_cruz(other)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
a = Algebra_Lineal(1, 2, -1)
b = Algebra_Lineal(2, -1, 0)
print("a =", a)
print("b =", b)
print("a + b =", a + b)           
print("a - b =", a - b)            
print("Producto cruz (a ^ b) =", a ^ b)  
print("Magnitud de a =", a.magnitud())
print("¿a es perpendicular a b? ", a.es_perpendicular(b))
print("¿a es paralelo a b?       ", a.es_paralelo(b))
print("Proyección de a sobre b =", a.proyeccion_sobre(b))
print("Componente de a en b =", a.componente_en(b))
