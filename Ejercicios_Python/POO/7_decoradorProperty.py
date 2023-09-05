# Decorador Property
class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
    
    @property # Decorador reservado para def un getter o setter
    def nombre(self):
        return self.__nombre

    @nombre.setter # Decorador para modificar
    def nombre(self, new_nombre):
        self.__nombre = new_nombre

    @nombre.deleter # Decorador para eliminar
    def nombre(self):
        del self.__nombre

jeferson = Persona("Jeferson", 34)

nombre = jeferson.nombre
print(nombre)

jeferson.nombre="Daniel"

nombre = jeferson.nombre
print(nombre)

del jeferson.nombre
print(nombre)