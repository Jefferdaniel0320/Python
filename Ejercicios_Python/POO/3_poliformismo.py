# Poliformismo

# Multiples formas
# en tipado dinamico no es necesario aplicar herencia, como lo es Python.

"""
Si fuera en JAva seria de la siguiete forma:

class Animal():
    def sonido(self):
        pass

class Gato(Animal):
    def sonido(self):
        return "Miau"

class Perro(Animal):
    def sonido(self):
        return "Guau"
"""


class Gato():
    def sonido(self):
        return "Miau"

class Perro():
    def sonido(self):
        return "Guau"

def hacer_sonido(animal): # 
    print(animal.sonido())

gato = Gato() # Objetos
perro = Perro()

print(perro.sonido()) # mando el mismo mensaje pero diferente objeto, esto es un poliformismo

hacer_sonido(perro) # esto es otro tipo de poliformmismo
