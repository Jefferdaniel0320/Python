# Script para generar DOM JS para Promerica
from openpyxl import load_workbook
import time
import subprocess
import os

print("Este programa genera Script para introducirlo en el CheckOut, recuerda cerrar todos los archivos:\n pasajeros.xlsx y mensajes.txt")
tipoProducto = input("Ingresa el tipo de producto v: Vuelos, c: Autos, a: Actividades, h: Hoteles, d: T.Disney\n")
nombre_archivo = "./pasajeros.xlsx"
libro_trabajo = load_workbook(nombre_archivo)
hoja = libro_trabajo.active
celdas_columna = hoja['A']
celdas_con_datos = sum(1 for celda in celdas_columna if celda.value is not None)

def infoPropietario ():
    archivo.write(f"var documentoIdentidad__0 = '{documentoIdentidad}';" + "\n")
    archivo.write(f"var numeroTel__0 = '{numeroTel}';" + "\n")
    archivo.write(f"var ciudad__0 = '{ciudad}';" + "\n")
    archivo.write(f"var direccion__0 = '{direccion}';" + "\n")
    archivo.write(f"var genero__0 = {genero}; // 0: hombre ; 1: mujer" + "\n")
    archivo.write(f"var nombre__0 = '{nombre}';" + "\n")
    archivo.write(f"var apellido__0 = '{apellido}';" + "\n")
    archivo.write(f"var fechaNacimineto__0 = '{fechaNacimiento}';" + "\n")
    archivo.write("var documentNumber = document.getElementById('documentNumber');" + "\n")
    archivo.write("documentNumber.value = documentoIdentidad__0;" + "\n")
    archivo.write("documentNumber.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")
    archivo.write("var phoneNumber = document.getElementById('phoneNumber');" + "\n")
    archivo.write("phoneNumber.value = numeroTel__0;" + "\n")
    archivo.write("phoneNumber.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")
    archivo.write("var city = document.getElementById('city');" + "\n")
    archivo.write("city.value = ciudad__0;" + "\n")
    archivo.write("city.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")
    archivo.write("var address = document.getElementById('address');" + "\n")
    archivo.write("address.value = direccion__0;" + "\n")
    archivo.write("address.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")

def pasajeros():
    archivo.write("var selectGender = document.getElementById('gender__0');" + "\n")
    archivo.write("selectGender.selectedIndex = genero__0;" + "\n")
    archivo.write("var name__0 = document.getElementById('name__0');" + "\n")
    archivo.write("name__0.value = nombre__0;" + "\n")
    archivo.write("name__0.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")
    archivo.write("var lastName__0 = document.getElementById('lastName__0');" + "\n")
    archivo.write("lastName__0.value = apellido__0;" + "\n")
    archivo.write("lastName__0.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")
    archivo.write("var documentNumber__0 = document.getElementById('documentNumber__0');" + "\n")
    archivo.write("documentNumber__0.value = documentoIdentidad__0;" + "\n")
    archivo.write("documentNumber__0.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")
    archivo.write("var birthDate__0 = document.getElementById('birthDate__0');" + "\n")
    archivo.write("birthDate__0.value = fechaNacimineto__0;" + "\n")
    archivo.write("birthDate__0.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")
    archivo.write("\n")

def pasajerosPruebas():
    archivo.write("var selectGender = document.getElementById('gender__0');" + "\n")
    archivo.write("selectGender.selectedIndex = genero__0;" + "\n")
    archivo.write("var name__0 = document.getElementById('name__0');" + "\n")
    archivo.write("name__0.value = nombre__0;" + "\n")
    archivo.write("name__0.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")
    archivo.write("var lastName__0 = document.getElementById('lastName__0');" + "\n")
    archivo.write("lastName__0.value = 'Pruebas UltraGroup';" + "\n")
    archivo.write("lastName__0.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")
    archivo.write("var documentNumber__0 = document.getElementById('documentNumber__0');" + "\n")
    archivo.write("documentNumber__0.value = documentoIdentidad__0;" + "\n")
    archivo.write("documentNumber__0.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")
    archivo.write("var birthDate__0 = document.getElementById('birthDate__0');" + "\n")
    archivo.write("birthDate__0.value = fechaNacimineto__0;" + "\n")
    archivo.write("birthDate__0.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")
    archivo.write("\n")

def vuelos():
    archivo.write("var passport = document.getElementById('passport__0');" + "\n")
    archivo.write(f"passport.value = {documentoIdentidad};" + "\n")
    archivo.write("passport.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")
    archivo.write("var expirationDate__0 = document.getElementById('expirationDate__0');" + "\n")
    archivo.write("expirationDate__0.value = '2030-12-31';" + "\n")
    archivo.write("expirationDate__0.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")
    archivo.write("\n")

for j in range(2):
    for i in range(2, celdas_con_datos + 1):
        if tipoProducto == "v":
            fila = 'A' + str(i)
        elif tipoProducto == "c":
            fila = 'B' + str(i)
        elif tipoProducto == "a" or tipoProducto == "h" or tipoProducto == "d":
            fila = 'C' + str(i)
        else:
            print("Ingresaste datos errados")
            break

        bandera = hoja[fila].value
        if bandera == 0:
            documentoIdentidad =    hoja['D' + str(i)].value
            numeroTel =             hoja['E' + str(i)].value
            ciudad =                hoja['F' + str(i)].value
            direccion =             hoja['G' + str(i)].value
            genero =                hoja['H' + str(i)].value
            nombre =                hoja['I' + str(i)].value
            apellido =              hoja['J' + str(i)].value
            fechaNacimiento =       str(hoja['K' + str(i)].value)[:10]
            hoja[fila] = 1
            break

    libro_trabajo.save(nombre_archivo)

    # Guardar los mensajes en un archivo de texto
    archivo_path = "mensajes.txt"
    with open(archivo_path, "w") as archivo:
        infoPropietario()
        if tipoProducto == "c":
            pasajeros()
        elif tipoProducto == "v":
            pasajeros()
            vuelos()
        elif tipoProducto == "h" or tipoProducto == "a" or tipoProducto == "d":
            pasajerosPruebas()
        else:
            print("Ingresaste datos errados")


# Abrir el archivo de texto con el Bloc de notas
subprocess.Popen(["notepad.exe", archivo_path])

# Esperar 8 segundos antes de cerrar la aplicación
time.sleep(8)

# Cerrar la aplicación después de 8 segundos
subprocess.run(["taskkill", "/f", "/im", "notepad.exe"], shell=True)

# Eliminar el archivo después de cerrar Notepad
# os.remove(archivo_path)
print("Script JS terminado...\n")