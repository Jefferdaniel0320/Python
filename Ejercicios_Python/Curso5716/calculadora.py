import datetime

print ("########################################")
print ("Bienvenido a la Calculadora")
print ("########################################")
print ("La opción 1 es para sumar")
print ("La opción 2 es para restar")
print ("La opción 3 es para multiplicar")
print ("La opción 4 es para dividir")
print ("La opción 0 es para finalizar el programa")
print ("La opción 9 es para ver el historial")
print ("########################################\n")

max_intentos = 3
intento = 0
operaciones = list()

def fechaHora():
    fecha_hora_actual = datetime.datetime.now()
    # fecha_hora_formateada = fecha_hora_actual.strftime("%H:%M:%S")
    fecha_hora_formateada = fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S")
    return fecha_hora_formateada

while True:
    operacion = float(input("Ingrese el tipo de operación que desea realizar: "))
    if operacion == 1:
        num1 = float(input("Ingrese el primer valor: "))
        num2 = float(input("Ingrese el segundo valor: "))
        res = round(float(num1 + num2),2)
        imprimir = f'Resultado: {num1} + {num2} = {res}'
        imprimirFecha = f'{fechaHora()} => {num1} + {num2} = {res}'
        print(imprimir)
        operaciones.append(imprimirFecha)
    elif operacion == 2:
        num1 = float(input("Ingrese el primer valor: "))
        num2 = float(input("Ingrese el segundo valor: "))
        res = round(float(num1 - num2),2)
        imprimir = f'Resultado: {num1} - {num2} = {res}'
        imprimirFecha = f'{fechaHora()} => {num1} - {num2} = {res}'
        print(imprimir)
        operaciones.append(imprimirFecha)
    elif operacion == 3:
        num1 = float(input("Ingrese el primer valor: "))
        num2 = float(input("Ingrese el segundo valor: "))
        res = round(float(num1 * num2),2)
        imprimir = f'Resultado: {num1} * {num2} = {res}'
        imprimirFecha = f'{fechaHora()} => {num1} * {num2} = {res}'
        print(imprimirFecha)
        operaciones.append(imprimirFecha)
    elif operacion == 4:
        num1 = float(input("Ingrese el primer valor: "))
        num2 = float(input("Ingrese el segundo valor: "))
        if num2 == 0:
            print("Error de Sintaxis, no se puede dividir entre 0")
        else:
            res = round(float(num1 / num2),2)
            imprimir = f'Resultado: {num1} / {num2} = {res}'
            imprimirFecha = f'{fechaHora()} => {num1} / {num2} = {res}'
            print(imprimir)
            operaciones.append(imprimirFecha)
    elif operacion == 0:
        print("Gracias por hacer uso de la calculadora \n El programa finalizo")
        break
    elif operacion == 9:
        print("############## Historial ###############")
        for operacion in operaciones:
            print(operacion)
        print("########################################\n")
    else:
        print("Marcaste una opcion incorrecta, vuelve a intentarlo")
        intento +=1
    
    if intento >= max_intentos:
        print("Superaste el maximo de errores permitidos")
        break