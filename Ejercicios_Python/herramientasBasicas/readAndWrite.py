
from openpyxl import load_workbook

# Nombre del archivo Excel
nombre_archivo = './ejemplo.xlsx'  # Cambia esto al nombre de tu archivo Excel

# Cargar el archivo Excel
libro_trabajo = load_workbook(nombre_archivo)

# Seleccionar la hoja de trabajo
hoja = libro_trabajo.active

# Leer el valor en la celda B2 y asignarlo a una variable
nombre = hoja['B2'].value

# Mostrar el valor original de B2
print(f"Valor original en B2: {nombre}")

# Modificar el valor en la celda B2
nuevo_nombre = 'Jeferson NUEVO'
hoja['B2'] = nuevo_nombre

# Leer el valor en la celda A2 y asignarlo a una variable
valor_a2 = hoja['A2'].value

# Mostrar el valor original en A2
print(f"Valor original en A2: {valor_a2}")

# Modificar el valor en la celda A2
nuevo_valor_a2 = 1
hoja['A2'] = nuevo_valor_a2

# Guardar los cambios en el mismo archivo Excel
libro_trabajo.save(nombre_archivo)
print("\nCambios guardados en el mismo archivo Excel.")
