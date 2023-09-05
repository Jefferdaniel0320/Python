# Decoradores
# Toma una funcion como entrada y le agrega un cod 
# extra y entrega la modificada.

def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la función")
        funcion()
        print("Despues de llamar a la función")
    return funcion_modificada

# Primera forma de hacerlo:
"""
def saludo():
    print("Hola Jeffer como andas")

saludo_modificado = decorador(saludo)
saludo_modificado()
"""

# Segunda forma de hacerlo, es la mas aconsejable:

@decorador
def saludo():
    print("Hola Jeffer como andas")

saludo()
