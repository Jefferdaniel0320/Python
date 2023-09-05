class Animal:
    def comer(self):
        print("puede comer")

class Mamifero(Animal):
    def amamantar(self):
        print("es Mamifero")
        
class Ave(Animal):
    def volar(self):
        print("puede volar")

class Murcielago(Mamifero,Ave):
    pass

murcielago = Murcielago()

murcielago.comer()
murcielago.amamantar()
murcielago.volar()

print(Murcielago.mro())
# RTA: [<class '__main__.Murcielago'>, <class '__main__.Mamifero'>, <class '__main__.Ave'>, <class '__main__.Animal'>, <class 'object'>]


