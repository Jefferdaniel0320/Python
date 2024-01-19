from openpyxl import load_workbook

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
        # fechaNacimiento2 = fechaNacimiento[0:10]
        # print(f"producto: {producto}, documentoIdentidad: {documentoIdentidad}, \nnumeroTel: {numeroTel}, ciudad: {ciudad}, \ndireccion: {direccion}, genero: {genero}, \nnombre: {nombre}, apellido: {apellido}, \nfechaNacimiento: {fechaNacimiento}")
        # scripJS(documentoIdentidad, numeroTel, ciudad, direccion, genero, nombre, apellido, fechaNacimiento)
        print(f"var documentoIdentidad = '{documentoIdentidad}';")
        print(f"var numeroTel = '{numeroTel}';")
        print(f"var ciudad = '{ciudad}';")
        print(f"var direccion = '{direccion}';")
        print(f"var genero = {genero}; // 0: hombre ; 1: mujer")
        print(f"var nombre = '{nombre}';")
        print(f"var apellido = '{apellido}';")
        print(f"var fechaNacimineto = '{fechaNacimiento}';")
        hoja['B' + str(i)] = 1
        break

"""
def scripJS(documentoIdentidad, numeroTel, ciudad, direccion, genero, nombre, apellido, fechaNacimiento):
    print(f"var documentoIdentidad = {documentoIdentidad};")
    print(f"var numeroTel = {numeroTel};")
    print(f"var ciudad = {ciudad};")
    print(f"var direccion = {direccion};")
    print(f"var genero = {genero}; // 0: hombre ; 1: mujer")
    print(f"var nombre = {nombre};")
    print(f"var apellido = {apellido};")
    print(f"var fechaNacimineto = {fechaNacimiento};")

    print("// Agregar Información del propietario")
    print("var documentNumber = document.getElementById('documentNumber');")
    print("documentNumber.value = documentoIdentidad;")
    print("documentNumber.dispatchEvent(new Event('input', { bubbles: true }));")
    print("var phoneNumber = document.getElementById('phoneNumber');")
    print("phoneNumber.value = numeroTel;")
    print("phoneNumber.dispatchEvent(new Event('input', { bubbles: true }));")
    print("var city = document.getElementById('city');")
    print("city.value = ciudad;")
    print("city.dispatchEvent(new Event('input', { bubbles: true }));")
    print("var address = document.getElementById('address');")
    print("address.value = direccion;")
    print("address.dispatchEvent(new Event('input', { bubbles: true }));")
    print("// Agregar Información de pasajeros")
    print("var selectGender = document.getElementById('gender__0');")
    print("selectGender.selectedIndex = genero;")
    print("var name__0 = document.getElementById('name__0');")
    print("name__0.value = nombre;")
    print("name__0.dispatchEvent(new Event('input', { bubbles: true }));")
    print("var lastName__0 = document.getElementById('lastName__0');")
    print("lastName__0.value = apellido;")
    print("lastName__0.dispatchEvent(new Event('input', { bubbles: true }));")
    print("var documentNumber__0 = document.getElementById('documentNumber__0');")
    print("documentNumber__0.value = documentoIdentidad;")
    print("documentNumber__0.dispatchEvent(new Event('input', { bubbles: true }));")
    print("var birthDate__0 = document.getElementById('birthDate__0');")
    print("birthDate__0.value = fechaNacimineto;")
    print("birthDate__0.dispatchEvent(new Event('input', { bubbles: true }));")
"""
libro_trabajo.save(nombre_archivo)
# print("\nCambios guardados en el mismo archivo Excel.")
