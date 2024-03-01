# Script para generar DOM JS para Promerica
from openpyxl import load_workbook
import re
import time
import subprocess
import os

print("\n****************************************************************************************************")
print("Este programa genera Script para introducirlo en el CheckOut para Promerica\nRecuerda cerrar todos los archivos:\nPasajeros.xlsx y mensajes.txt")
print("****************************************************************************************************")
nuevaConsulta = True
while nuevaConsulta:
    url = input("\nIngresa la URL de la Disponibilidad:\n")
    # URL´s de Prueba PDN:
    # https://viajeky.grupopromerica.com/flights/availability/round/20240302_MIA_JFK-20240303_JFK_MIA/all/economy/all-stops/international/1_adult/1_child/1_infant
    # https://viajesky.grupopromerica.com/cars/recommendations/MIA-MIA/2024-03-08_1200/2024-03-09_1200/standard?payment=online
    # https://viajeky.grupopromerica.com/hotels/search/MIA/2024-03-01/2024-03-02/1-adults_0-children?nationality=KY
    # https://viajeky.grupopromerica.com/disney/results/2-days/1-adults/0-children/2024-03-23
    # https://viajeky.grupopromerica.com/activities/MIA/2024-03-05/2024-03-05/passengers-18,19,17,12
    
    # URL´s de Prueba DEMO:
    # https://traveldemo-pmerica-ky.smartlinks.dev/flights/availability/round/20240912_MIA_MEX-20240913_MEX_MIA/all/economy/all-stops/international/2_adult/0_child/0_infant
    # https://demo-pmerica-ky.smartlinks.dev/cars/recommendations/MIA-MIA/2024-10-16_1200/2024-10-18_1200/standard?payment=online
    # https://traveldemo-pmerica-ky.smartlinks.dev/hotels/search/MIA/2024-10-16/2024-10-18/2-adults_0-children-11?nationality=KY
    # https://traveldemo-pmerica-ky.smartlinks.dev/disney/results/2-days/1-adults/0-children/2024-10-16
    # https://traveldemo-pmerica-ky.smartlinks.dev/activities/MIA/2024-10-16/2024-10-16/passengers-20,11,24,10

    # Expresión regular para encontrar los valores de adulto, niño e infante
    patronProducto = r"pmerica\-ky\.smartlinks\.dev/([^/]+)/" # Demo
    # patronProducto = r"grupopromerica\.com/([^/]+)/" # PDN

    # Buscar los valores en la URL usando la expresión regular
    resultadoProducto = re.search(patronProducto, url).group(1)

    # Datos Archivo Excel
    nombre_archivo = "./pasajeros.xlsx"
    libro_trabajo = load_workbook(nombre_archivo)
    hoja = libro_trabajo.active
    
    print("\n------------------------------")    
    
    if resultadoProducto == "flights":
        tipoProducto = "v"
        celdas_columna = hoja['A']
        patronTotalPasajeros = r"/(\d+)_adult/(\d+)_child/(\d+)_infant"
        resultadoTotalPasajeros = re.search(patronTotalPasajeros, url)

        # Extraer los valores encontrados
        if resultadoTotalPasajeros:
            adulto = int(resultadoTotalPasajeros.group(1))
            niño = int(resultadoTotalPasajeros.group(2))
            infante = int(resultadoTotalPasajeros.group(3))
        print("El Producto de la URL es: Vuelos")

    elif resultadoProducto == "cars":
        tipoProducto = "c"
        celdas_columna = hoja['B']
        adulto , niño , infante = 1 , 0 , 0
        print("El Producto de la URL es: Autos")

    elif resultadoProducto == "activities": # PENDIETE
        tipoProducto = "a"
        celdas_columna = hoja['C']
        adulto = int(input("Agrega la cantidad de pasajeros: "))
        niño , infante = 0 , 0
        print("El Producto de la URL es: Actividades")

    elif resultadoProducto == "hotels":
        tipoProducto = "h"
        celdas_columna = hoja['C']
        patronTotalPasajeros = r"/(\d+)-adults_(\d+)-children"
        resultadoTotalPasajeros = re.search(patronTotalPasajeros, url)
        # Extraer los valores encontrados
        if resultadoTotalPasajeros:
            adulto = int(resultadoTotalPasajeros.group(1))
            niño = int(resultadoTotalPasajeros.group(2))
            infante = 0
        print("El Producto de la URL es: Hoteles")

    elif resultadoProducto == "disney":
        tipoProducto = "d"
        celdas_columna = hoja['C']
        patronTotalPasajeros = r"/(\d+)-adults/(\d+)-children/"
        resultadoTotalPasajeros = re.search(patronTotalPasajeros, url)
        # Extraer los valores encontrados
        if resultadoTotalPasajeros:
            adulto = int(resultadoTotalPasajeros.group(1))
            niño = int(resultadoTotalPasajeros.group(2))
            infante = 0
        print("El Producto de la URL es: Disney")

    cantidadPasajeros = adulto + niño + infante
    print(f"La cantidad de pasajeros es de {cantidadPasajeros}")
    print("------------------------------\n")
    
    celdas_con_datos = sum(1 for celda in celdas_columna if celda.value is not None)
    celdas_con_datos_cero = sum(1 for celda in celdas_columna if celda.value is not None and celda.value == 0)

    # print(f"celdas_con_datos {celdas_con_datos}")
    # print(f"celdas_con_datos_cero {celdas_con_datos_cero}")

    if celdas_con_datos_cero < cantidadPasajeros:
        print(f"Se están solicitando datos para {cantidadPasajeros} pasajeros, pero solo se cuenta con {celdas_con_datos_cero} datos en la tabla de Excel. \nSe requiere validar el archivo pasajeros.xls para modificar los valores o agregar más filas de datos")
        break

    def infoPropietario ():
        archivo.write("// Información del Propietario" + "\n")
        archivo.write("var documentNumber = document.getElementById('documentNumber');" + "\n")
        archivo.write(f"documentNumber.value = {documentoIdentidad};" + "\n")
        archivo.write("documentNumber.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")
        archivo.write("var phoneNumber = document.getElementById('phoneNumber');" + "\n")
        archivo.write(f"phoneNumber.value = {numeroTel};" + "\n")
        archivo.write("phoneNumber.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")
        archivo.write("var city = document.getElementById('city');" + "\n")
        archivo.write(f"city.value = '{ciudad}';" + "\n")
        archivo.write("city.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")
        archivo.write("var address = document.getElementById('address');" + "\n")
        archivo.write(f"address.value = '{direccion}';" + "\n")
        archivo.write("address.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")
        archivo.write("var cuadro = document.getElementById('conditions');" + "\n")
        archivo.write("cuadro.click();" + "\n")
        archivo.write("\n")

    def pasajeros(i):
        archivo.write(f"// Información del pasajero {i+1}" + "\n")
        archivo.write(f"var selectGender = document.getElementById('gender__{i}');" + "\n")
        archivo.write(f"selectGender.selectedIndex = {genero};" + "\n")
        archivo.write(f"var name__{i} = document.getElementById('name__{i}');" + "\n")
        archivo.write(f"name__{i}.value = '{nombre}';" + "\n")
        archivo.write(f"name__{i}.dispatchEvent(new Event('input', {{ bubbles: true }}));" + "\n")
        archivo.write(f"var lastName__{i} = document.getElementById('lastName__{i}');" + "\n")
        archivo.write(f"lastName__{i}.value = '{apellido}';" + "\n")
        archivo.write(f"lastName__{i}.dispatchEvent(new Event('input', {{ bubbles: true }}));" + "\n")
        archivo.write(f"var documentNumber__{i} = document.getElementById('documentNumber__{i}');" + "\n")
        archivo.write(f"documentNumber__{i}.value = {documentoIdentidad};" + "\n")
        archivo.write(f"documentNumber__{i}.dispatchEvent(new Event('input', {{ bubbles: true }}));" + "\n")
        archivo.write(f"var birthDate__{i} = document.getElementById('birthDate__{i}');" + "\n")
        archivo.write(f"birthDate__{i}.value = '{fechaNacimiento}';" + "\n")
        archivo.write(f"birthDate__{i}.dispatchEvent(new Event('input', {{ bubbles: true }}));" + "\n")
        archivo.write("\n")

    def pasajerosPruebas(i):
        archivo.write(f"// Información del pasajero {i+1}" + "\n")
        archivo.write(f"var selectGender = document.getElementById('gender__{i}');" + "\n")
        archivo.write(f"selectGender.selectedIndex = {genero};" + "\n")
        archivo.write(f"var name__{i} = document.getElementById('name__{i}');" + "\n")
        archivo.write(f"name__{i}.value = '{nombre}';" + "\n")
        archivo.write(f"name__{i}.dispatchEvent(new Event('input', {{ bubbles: true }}));" + "\n")
        archivo.write(f"var lastName__{i} = document.getElementById('lastName__{i}');" + "\n")
        archivo.write(f"lastName__{i}.value = '{apellido} Pruebas UltraGroup';" + "\n")
        archivo.write(f"lastName__{i}.dispatchEvent(new Event('input', {{ bubbles: true }}));" + "\n")
        archivo.write(f"var documentNumber__{i} = document.getElementById('documentNumber__{i}');" + "\n")
        archivo.write(f"documentNumber__{i}.value = {documentoIdentidad};" + "\n")
        archivo.write(f"documentNumber__{i}.dispatchEvent(new Event('input', {{ bubbles: true }}));" + "\n")

    def pasajerosPruebasbirthDate(i):
        archivo.write(f"var birthDate__{i} = document.getElementById('birthDate__{i}');" + "\n")
        archivo.write(f"birthDate__{i}.value = '{fechaNacimiento}';" + "\n")
        archivo.write(f"birthDate__{i}.dispatchEvent(new Event('input', {{ bubbles: true }}));" + "\n")
        archivo.write("\n")

    def vuelos(i):
        archivo.write("// Información del pasajero sección Vuelos" + "\n")
        archivo.write(f"var passport = document.getElementById('passport__{i}');" + "\n")
        archivo.write(f"passport.value = {documentoIdentidad};" + "\n")
        archivo.write("passport.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")
        archivo.write(f"var expirationDate__{i} = document.getElementById('expirationDate__{i}');" + "\n")
        archivo.write(f"expirationDate__{i}.value = '2030-12-31';" + "\n")
        archivo.write(f"expirationDate__{i}.dispatchEvent(new Event('input', {{ bubbles: true }}));" + "\n")
        archivo.write("\n")

    # Guardar los mensajes en un archivo de texto
    archivo_path = "mensajes.txt"
    # Apertura del archivo
    archivo = open(archivo_path, "w")
    
    for j in range(cantidadPasajeros):
        for i in range(2, celdas_con_datos + 1):
            if tipoProducto == "v":
                fila = 'A' + str(i)
            elif tipoProducto == "c":
                fila = 'B' + str(i)
            elif tipoProducto == "a" or tipoProducto == "h" or tipoProducto == "d":
                fila = 'C' + str(i)

            bandera = hoja[fila].value
            if bandera == 0:
                documentoIdentidad =    hoja['D' + str(i)].value
                numeroTel =             hoja['E' + str(i)].value
                ciudad =                hoja['F' + str(i)].value
                direccion =             hoja['G' + str(i)].value
                genero =                hoja['H' + str(i)].value
                nombre =                hoja['I' + str(i)].value
                apellido =              hoja['J' + str(i)].value
                
                if j+1 <= adulto:
                    fechaNacimiento =   str(hoja['K' + str(i)].value)[:10]
                elif j+1 >= niño and j+1 <= adulto + niño:
                    fechaNacimiento =   '2016-01-01'
                elif j+1 >= adulto + niño:
                    fechaNacimiento =   '2023-01-01'
                hoja[fila] = 1
                break

        libro_trabajo.save(nombre_archivo)  

        # Llenado del archivo .txt
        if j == 0:
            infoPropietario()
        if tipoProducto == "c":
            pasajeros(j)
        elif tipoProducto == "v":
            pasajeros(j)
            vuelos(j)
        elif tipoProducto == "a":
            pasajerosPruebas(j)
            archivo.write("\n")
        elif tipoProducto == "h" or tipoProducto == "d":
            pasajerosPruebas(j)
            pasajerosPruebasbirthDate(j)
        else:
            print("Ingresaste datos errados")

    # Cierre manual del archivo
    archivo.close()

    # Abrir el archivo de texto con el Bloc de notas
    subprocess.Popen(["notepad.exe", archivo_path])

    # Esperar 8 segundos antes de cerrar la aplicación
    time.sleep(8)

    # Cerrar la aplicación después de 8 segundos
    subprocess.run(["taskkill", "/f", "/im", "notepad.exe"], shell=True)

    # Eliminar el archivo después de cerrar Notepad
    # os.remove(archivo_path)
    
    # bucle while
    programa = input("Desea continuar haciendo pruebas, s: si n: no\n")
    if programa == "n" or programa == "N":
        nuevaConsulta = False

print("Script JS terminado...\n")
