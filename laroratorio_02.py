import math

class algebralineal:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
    
    def __add__(self, other):
        return algebralineal(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return algebralineal(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        """ Producto punto """
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __xor__(self, other):
        """ Producto cruz """
        return algebralineal(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def magnitud(self):
        """ Magnitud del vector """
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def es_perpendicular(self, other):
        return self * other == 0  # Producto punto == 0

    def es_paralelo(self, other):
        return self ^ other == algebralineal(0, 0, 0)  # Producto cruz == 0

    def proyeccion_sobre(self, other):
        coef = (self * other) / (other.magnitud() ** 2)
        return algebralineal(coef * other.x, coef * other.y, coef * other.z)

    def componente_en(self, other):
        return (self * other) / other.magnitud()

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


v1= algebralineal(1, 2, -1)
v2 = algebralineal(2, -1, 0)


print("Es perpendicular?", v1.es_perpendicular(v2))
print("Es paralelo?", v1.es_paralelo(v2))
print("Proyección de a sobre b:", v1.proyeccion_sobre(v2))
print("Componente de a en b:", v1.componente_en(v2))
