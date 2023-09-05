class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def nombreEdad(self):
        print(f'El nombre de la persona es {self.nombre} y la edad es {self.edad} años')

class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado = grado
    
    def graducacion(self):
        print(f'El estudiante esta en el grado {self.grado}')

marco = Estudiante("Marco Romero", 30, "10")

marco.nombreEdad()
marco.graducacion()

