# Valores
print('--------------------')
juguete = 15
print(f'Precio del juguete: {juguete}')
juguete = 12
print(f'Precio nuevo del juguete: {juguete}')
print('--------------------')
caramelos = 5
precio = 2
costo = caramelos * precio
print(f'El precio de los caramelos es de: {costo}')
caramelos = 8
precio = 3
costo = caramelos * precio
print(f'El precio de los caramelos es de: {costo}')
print('--------------------')
ahorro = 15
ahorro = ahorro + 10
ahorro = ahorro - 2
ahorro = ahorro + 5
ahorro = ahorro - 7
print(f'Nos quedo: {ahorro} Euros')
print('--------------------')
pTotales = 46
pOcupadas = 32
pReservadas = 14
pVacias = pTotales - (pOcupadas + pReservadas)
autobusLleno = pTotales == (pOcupadas + pReservadas)
print(f'Plazas Vacias: {pVacias}')
print(f'Autobus Lleno: {autobusLleno}')
print('--------------------')
puntosTotales = 100
nivel1 = 48
nivel2 = 62
puntosConseguidos = nivel1 + nivel2
comparacion = puntosConseguidos >= puntosTotales
print(f'Los puntos conseguidos son mayores o iguales a los que se deben conseguir: {comparacion}')
print('--------------------')
dato = 5
datoMetros = dato * 1000
datoCentimetros = datoMetros * 100
print(f'{dato}KM corresponde a {datoMetros}m y a {datoCentimetros}cm')
print('--------------------')
dia = 3
horas = dia * 24
minutos = horas * 60
print(f'{dia} días corresponden a {horas} horas y a {minutos} minutos')
print('--------------------')
# Cambiar el valor de una variable por el valor de la otra:
juan = 200
maria = 15
print(f'juan = {juan}, maria = {maria}')
temporal = juan
juan = maria
maria = temporal
print(f'juan = {juan}, maria = {maria}')
print('--------------------')
# Asignacion multiple
jeferson, marco = 34 , 30
print(f'jeferson = {jeferson}, marco = {marco}')
jeferson, marco = marco, jeferson
print(f'jeferson = {jeferson}, marco = {marco}')
print('--------------------')
