# Metodo de resolucion de orden

class A:
    #pass
    def hablar(self):
        print("Hola desde A")

class B(A):
    #pass
    def hablar(self):
        print("Hola desde B")

class C(A):
    #pass
    def hablar(self):
       print("Hola desde C")

class D(B,C): # aca elije primero B y si no existe va luego por C
    #pass
    def hablar(self):
        print("Hola desde D")

d = D()
d.hablar()

print(D.mro()) # esto sirve para ver como va la herencia.

"""
aca parte desde D, elige B, luego C y por ultimo A
        A
      *   *
    *       *
  *           *
B               C
  *           *
    *       *
      *   * 
        D

aca elige primero B y mira la rama completa, es decir mira hasta A, despues de esta revisa la rama C hasta la F
 A       F
 *       *
 *       *
 *       *
 B       C
  *     *
   *   *
    * *
     D

"""