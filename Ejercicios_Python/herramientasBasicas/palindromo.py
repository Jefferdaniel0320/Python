
# Programa que evalua si un string es Palindromo o no

bandera = True
contador = 0
while bandera:
    def palindromo(cadena):
        cadena = cadena.lower()
        cadenaLimpia = ''

        for caracter in cadena:
            if caracter != ' ':
                cadenaLimpia += caracter

        longitud = len(cadenaLimpia)

        for letra in range(longitud//2):
            if cadenaLimpia[letra] != cadenaLimpia[longitud-letra-1]:
                return False
        return True
    if contador == 0:
        print('***********************************************************************')
        print('Este es un programa que evalua si una palabra o una frase es Palindromo')
        print('***********************************************************************')
    palabra = input('Ingresa una palabra o frase: ')
    # palabra = 'se verlas al reves'
    # palabra = 'Reconocer'
    # palabra = 'anita lava la tina'
    
    if palindromo(palabra):
        print(f'\n"{palabra}" Es un palíndromo, ya que se lee igual de izquierda a derecha que de derecha a izquierda.\n')
    else:
        print(f'"{palabra}" No es un palindromo\n')

    contador += 1
    validacion = input('¿Quieres continuar validando strings? (s/n): ').lower()

    if validacion != 's':
        bandera = False
        print('\nEl programa finaizo correctamente...\n')
    

"""
# Otra forma de resolverlo con las funciones especiales de Python

def es_palindromo(cadena):
    # Convertir la cadena a minúsculas
    cadena = cadena.lower()
    
    # Eliminar los espacios en blanco
    cadena_sin_espacios = cadena.replace(" ", "")
    
    # Verificar si la cadena sin espacios es igual a su inversa utilizando slicing
    return cadena_sin_espacios == cadena_sin_espacios[::-1]

cadena = input("Ingresa una cadena: ")
if es_palindromo(cadena):
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")

"""