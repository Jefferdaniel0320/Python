# Getters

class Persona:
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad
    
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, new_nombre):
        self._nombre = new_nombre

jeferson = Persona("Jeferson", 21)

nombre = jeferson.get_nombre()
print(nombre)

jeferson.set_nombre("Daniel")

nombre = jeferson.get_nombre()
print(nombre)