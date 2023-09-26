"""
while True:
    nota1 = float(input("Ingresar la Primera nota: "))
    nota2 = float(input("Ingresar la Segunda nota: "))
    nota3 = float(input("Ingresar la Tercera nota: "))

    if 1 <= nota1 <= 10 and 1 <= nota2 <= 10 and 1 <= nota3 <= 10:
        promedio = (nota1 + nota2 + nota3) / 3

        if promedio > 9:
            mensaje = "Felicitaciones"
        elif 8 <= promedio <= 8.9:
            mensaje ="Buen Trabajo"
        elif 6 <= promedio <= 7.9:
            mensaje ="Regular"
        elif 4 <= promedio <= 5.9:
            mensaje ="Malo"
        else:
            mensaje ="Muy malo"
        
        print("\n**************************************")
        print(f'El promedio es de {promedio}')
        print(f'Mensaje: {mensaje}')
        print("**************************************")
        
        nuevoPromedio = input("\n Para volver a calcular el promedio, escribe \"Si\" \n De lo contrario, escribe \"Salir\" \n")
        
        if nuevoPromedio.lower() != "si":
            break
    else:
        print("Error, las notas deben estar entre 1 y 10, intentalo nuevamente:\n")
"""
#"""
while True:
    notas = list()
    max_intentos = 3  # Establece el límite de intentos
    
    print("Vamos a calcular el promedio de notas, la calificación debe estar entre 1 y 10")
    cantidadNotas = int(input("Escribe el número de notas que deseas agregar:\n"))
    
    intentos = 0  # Inicializa el contador de intentos
    
    for i in range(cantidadNotas):
        while True:
            nota = float(input(f"Agrega la nota {i + 1}: "))
            if 1 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("Error, la calificación debe estar entre 1 y 10")
                intentos += 1  # Incrementa el contador de intentos
                
                if intentos >= max_intentos:
                    print("Se superó el límite de errores")
                    break
        if intentos >= max_intentos:
            break
    
    if intentos >= max_intentos:
        break # salimos del ciclo while
    
    print(f"Notas: {notas}")
    
    if len(notas) > 0:
        promedio = sum(notas) / len(notas)
    else:
        print("No se ingresaron notas.")
        continue
    
    if promedio > 9:
        mensaje = "Excelente"
    elif 8 <= promedio <= 8.9:
        mensaje = "Sobresaliente"
    elif 6 <= promedio <= 7.9:
        mensaje = "Regular"
    elif 4 <= promedio <= 5.9:
        mensaje = "Malo"
    else:
        mensaje = "Muy Malo"

    print(f'Te queremos informar que tu resultado fue: {mensaje}, esto se debe a que tu promedio fue de: {round(promedio, 2)}')
    
    nuevoPromedio = input("¿Deseas calcular otro promedio? (Si/No): ").lower()
    if nuevoPromedio != "si":
        break
#"""
