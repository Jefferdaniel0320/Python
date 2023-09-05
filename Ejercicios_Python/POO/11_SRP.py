# Ejercicio de

class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100

    def agregarCombustible(self,cantidad):
        self.combustible += cantidad
    
    def obtenerCombustible(self):
        return self.combustible
    
    def usarCombustible(self, cantidad):
        self.combustible -= cantidad

class Auto():
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque
    
    def mover(self, distancia):
        if self.tanque.obtenerCombustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usarCombustible(distancia / 2)
            print("Has movido el auto exitosamente")
        else:
            print("No hay suficiente combustible")

    def obtenerPosicion(self):
        return self.posicion

tanque = TanqueDeCombustible()
roquita = Auto(tanque)

print(roquita.obtenerPosicion())
roquita.mover(10)
print(roquita.obtenerPosicion())
roquita.mover(20)
print(roquita.obtenerPosicion())
roquita.mover(60)
print(roquita.obtenerPosicion())
roquita.mover(100)
print(roquita.obtenerPosicion())
roquita.mover(100)
print(roquita.obtenerPosicion())
