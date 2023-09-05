
class Estudiante:
    def __init__ (self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
    
    def estudiar(self):
        print(f'el estudiante {self.nombre} esta estudiando')

nombre = input ("Digame su nombre: ")
edad   = input ("Ahora su edad: ")
profesion  = input ("por ultimo, su profesion: ")

estudiante = Estudiante(nombre,edad,profesion)

print(f"""
    DATOS DEL ESTUDIANTE: \n
    Nombre: {estudiante.nombre} \n
    edad: {estudiante.edad} \n
    Profesion: {estudiante.profesion} \n
    """)
count = 0

while True:
    estudiar = input("Que esta haciendo el estudiante? \n")
    if count > 3:
        print("Exediste la cantidad de intentos")
        break
    elif estudiar.lower() == "salir":
        print("Saliste del programa")
        break
    count += 1
    print("si quieres salir, escribe salir \n")
    if(estudiar.lower() == "estudiar"):
        estudiante.estudiar()
        break