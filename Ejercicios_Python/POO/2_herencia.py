# Herencia
# Esta la Herencia simple que seria Persona que es la padre
# la hija es empleado, o podria ser gerarquica, que seria persona como padre
# empleados, estuadiante y jefe, serian las clases que dependen de persona.

class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def presentacion(self):
        print(f'La persona es {self.nombre} con la edad de {self.edad} años y la nacionalidad {self.nacionalidad}')

class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
    def trabaja(self):
        print(f'La persona es {self.nombre} con la edad de {self.edad} años y la nacionalidad {self.nacionalidad} trabaja en {self.trabajo} con un salario de {self.salario} millones')

class Estudiante(Persona):
    def __init__(self,nombre,edad,nacionalidad,notas,universidad):
        super().__init__(nombre,edad,nacionalidad)
        self.notas = notas
        self.universidad = universidad

class jefe(Persona):
    pass # Esto significa que no hace nada, para que no genere errores

marco = Empleado("Marco Romero", 30, "Colombiano", "Programacion", "$5.000.000")

marco.presentacion()
marco.trabaja()