# Script para generar DOM JS
from openpyxl import load_workbook
import time
import subprocess
import os

nombre_archivo = "./pasajeros.xlsx"
libro_trabajo = load_workbook(nombre_archivo)
hoja = libro_trabajo.active

celdas_columna = hoja['A']
celdas_con_datos = sum(1 for celda in celdas_columna if celda.value is not None)

for i in range(2, celdas_con_datos + 1):
    bandera = hoja['B' + str(i)].value
    if bandera == 0:
        producto =              hoja['A' + str(i)].value
        documentoIdentidad =    hoja['C' + str(i)].value
        numeroTel =             hoja['D' + str(i)].value
        ciudad =                hoja['E' + str(i)].value
        direccion =             hoja['F' + str(i)].value
        genero =                hoja['G' + str(i)].value
        nombre =                hoja['H' + str(i)].value
        apellido =              hoja['I' + str(i)].value
        fechaNacimiento =       str(hoja['J' + str(i)].value)[:10]

        text_documentoIdentidad = f"var documentoIdentidad = '{documentoIdentidad}';"
        text_numeroTel = f"var numeroTel = '{numeroTel}';"
        text_ciudad = f"var ciudad = '{ciudad}';"
        text_direccion = f"var direccion = '{direccion}';"
        text_genero = f"var genero = {genero}; // 0: hombre ; 1: mujer"
        text_nombre = f"var nombre = '{nombre}';"
        text_apellido = f"var apellido = '{apellido}';"
        text_fechaNacimiento = f"var fechaNacimineto = '{fechaNacimiento}';"
        # Vuelos
        text_pasaporte = f"passport.value = {documentoIdentidad};"
        
        hoja['B' + str(i)] = 1
        break

libro_trabajo.save(nombre_archivo)
# print("\nCambios guardados en el mismo archivo Excel.")

def infoPropietario ():
    archivo.write(text_documentoIdentidad + "\n")
    archivo.write(text_numeroTel + "\n")
    archivo.write(text_ciudad + "\n")
    archivo.write(text_direccion + "\n")
    archivo.write(text_genero + "\n")
    archivo.write(text_nombre + "\n")
    archivo.write(text_apellido + "\n")
    archivo.write(text_fechaNacimiento + "\n")
    archivo.write("var documentNumber = document.getElementById('documentNumber');" + "\n")
    archivo.write("documentNumber.value = documentoIdentidad;" + "\n")
    archivo.write("documentNumber.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")
    archivo.write("var phoneNumber = document.getElementById('phoneNumber');" + "\n")
    archivo.write("phoneNumber.value = numeroTel;" + "\n")
    archivo.write("phoneNumber.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")
    archivo.write("var city = document.getElementById('city');" + "\n")
    archivo.write("city.value = ciudad;" + "\n")
    archivo.write("city.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")
    archivo.write("var address = document.getElementById('address');" + "\n")
    archivo.write("address.value = direccion;" + "\n")
    archivo.write("address.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")

def pasajeros():
    archivo.write("var selectGender = document.getElementById('gender__0');" + "\n")
    archivo.write("selectGender.selectedIndex = genero;" + "\n")
    archivo.write("var name__0 = document.getElementById('name__0');" + "\n")
    archivo.write("name__0.value = nombre;" + "\n")
    archivo.write("name__0.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")
    archivo.write("var lastName__0 = document.getElementById('lastName__0');" + "\n")
    archivo.write("lastName__0.value = apellido;" + "\n")
    archivo.write("lastName__0.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")
    archivo.write("var documentNumber__0 = document.getElementById('documentNumber__0');" + "\n")
    archivo.write("documentNumber__0.value = documentoIdentidad;" + "\n")
    archivo.write("documentNumber__0.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")
    archivo.write("var birthDate__0 = document.getElementById('birthDate__0');" + "\n")
    archivo.write("birthDate__0.value = fechaNacimineto;" + "\n")
    archivo.write("birthDate__0.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")

def pasajerosPruebas():
    archivo.write("var selectGender = document.getElementById('gender__0');" + "\n")
    archivo.write("selectGender.selectedIndex = genero;" + "\n")
    archivo.write("var name__0 = document.getElementById('name__0');" + "\n")
    archivo.write("name__0.value = nombre;" + "\n")
    archivo.write("name__0.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")
    archivo.write("var lastName__0 = document.getElementById('lastName__0');" + "\n")
    archivo.write("lastName__0.value = 'Pruebas UltraGroup';" + "\n")
    archivo.write("lastName__0.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")
    archivo.write("var documentNumber__0 = document.getElementById('documentNumber__0');" + "\n")
    archivo.write("documentNumber__0.value = documentoIdentidad;" + "\n")
    archivo.write("documentNumber__0.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")
    archivo.write("var birthDate__0 = document.getElementById('birthDate__0');" + "\n")
    archivo.write("birthDate__0.value = fechaNacimineto;" + "\n")
    archivo.write("birthDate__0.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")

def vuelos():
    archivo.write("var passport = document.getElementById('passport__0');" + "\n")
    archivo.write(text_pasaporte + "\n")
    archivo.write("passport.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")
    archivo.write("var expirationDate__0 = document.getElementById('expirationDate__0');" + "\n")
    archivo.write("expirationDate__0.value = '2030-12-31';" + "\n")
    archivo.write("expirationDate__0.dispatchEvent(new Event('input', { bubbles: true }));" + "\n")

# Guardar los mensajes en un archivo de texto
archivo_path = "mensajes.txt"
with open(archivo_path, "w") as archivo:
    producto = input("Ingresa el tipo de producto v: Vuelos, c: Autos, a: Actividades, h: Hoteles, d: T.Disney\n")
    if producto == "c":
        infoPropietario()
        pasajeros()
    elif producto == "v":
        infoPropietario()
        pasajeros()
        vuelos()
    elif producto == "h" or producto == "a" or producto == "d":
        infoPropietario()
        pasajerosPruebas()
        vuelos()
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
