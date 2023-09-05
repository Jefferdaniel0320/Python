# Herencia Multiple

class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print("Hola, estoy hablando un poco")
    
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        return f"Mi habilidad es {self.habilidad}"

class EmpleadoArtista(Persona,Artista):
    def __init__(self,nombre,edad,nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        print(f'Hola, soy {self.nombre}, {self.mostrar_habilidad()} y trabajo en la empresa {self.empresa}.')

marco = EmpleadoArtista("Marco Romero",30,"Colombiano","Programar","$ 5.000.000","DNP")
marco.presentarse()

herencia = issubclass(EmpleadoArtista,Persona)
print("EmpleadoArtista hereda de Artista: ", herencia) #Es decir, EmpleadoArtista es una subclase de Artista

instancia = isinstance(marco,EmpleadoArtista)
print("marco es un objeto de EmpleadoArtista: ", instancia)

instancia2 = isinstance(marco,Artista)
print("marco es un objeto de Artista: ", instancia2)