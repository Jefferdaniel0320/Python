# Este programa calcula la división de dos numeros sin utilizar los simbolos de Multiplicación y División

bandera = True
validacion = 'n'

while bandera:
    def division( x,y ):
        valorModulo = x%y
        valorDividendo = x
        valorDiviosr = y

        contador = 1
        contador2 = 0.0
        
        if x < y:
            contador = 0
            contador2 = 0.1
            for i in range(9):
                x += valorDividendo
            while x > y:
                x -= y
                contador2 += 0.1
            if y > x:
                contador -=0.1

        elif x % y == 0:
            while x > y:
                x -= y
                contador += 1

        elif x % y !=0:
            while x > y:
                x -= y
                contador += 1
                if y > x:
                    contador -=1
            for i in range(10):
                x += valorModulo
            while x > y:
                x -= y
                contador2 += 0.1

        return contador + contador2

    x = int(input('Ingresa el Dividendo numero: '))
    y = int(input('Ingresa el Divisor numero: '))

    if y == 0:
        print('No es posible dividir por 0, vuelve a intentarlo')
    else:
        print(f'El resultado de la División es: {division(x,y)}')
        validacion = input('¿Quieres continuar validando strings? (s/n): ').lower()

    if validacion != 's':
        bandera = False
        print('\nEl programa finaizo correctamente...\n')
