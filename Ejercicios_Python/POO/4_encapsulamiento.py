# Encapsulamiento
# En Python, no son totalmente privados

class MiClase:
    def __init__(self):
        self._atributo_privado = "Valor" # al tener solo 1 "_" no lo hace tan privado
        #self.__atributo_privado = "Valor Privado" # De esta forma es totalmente privado


objeto = MiClase()
print(objeto._atributo_privado)
#print(objeto.__atributo_privado)

