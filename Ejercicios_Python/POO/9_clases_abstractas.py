# Clases Abstractas
from abc import ABC, abstractclassmethod
# abstractclassmethod es un decorador

class Persona(ABC):
    @abstractclassmethod # con esto se dice que estamods creando un metodo abstracto. 
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractclassmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_actividad(self):
        print(f"Estoy estudiando {self.actividad}")

class Trabajador (Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_actividad(self):
        print(f"Actualmente estoy trabajando en el rublo de {self.actividad}")

marco = Estudiante("Marco Andrey Romero",30,"Masculino","Programación")
jeferson = Trabajador("Jeferson Daniel Romero",35,"Maculino","Ing Proyectos")

marco.presentarse()
marco.hacer_actividad()
jeferson.presentarse()
jeferson.hacer_actividad()
