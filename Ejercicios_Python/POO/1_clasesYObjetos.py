
# CLASES

# las clases inician en Mayuscula
class CelularFijo():
    marcaf = "Samsung" # Atributos fijos
    modelof = "S23"
    camaraf = "48MP"

celular1 = CelularFijo() # Esto es un Objeto y CelularFijo() es instancia del objeto 
celular2 = CelularFijo()
celular3 = CelularFijo()

#print(celular1.camara)

# ----------------------------

class Celular:
    # init es un metodo especial
    def __init__(self, marca, modelo, camara): # Esto se llama metodo constructor y se ejecuta de primeras
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self): # esto es un metodo
        print("Estas haciendo una llamada") 
        
    def cortar(self):
        print("Cortaste la llamada")
    
    def llamar_modelo(self):
        print(f'Estas haciendo una llamada desde un: {self.modelo}')
    
    def cortar_modelo(self):
        print(f'Cortaste la llamada desde tu: {self.modelo}')


celular1 = Celular("Samsung", "S23", "48MP")
celular2 = Celular("Apple", "Iphone 15 Pro", "96MP")

print(celular2.marca)

# !Metodos
# Un metodo es una funcion

celular1.llamar()
celular1.llamar_modelo()


