"""
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
"""

from borrarPantalla import borrarPantalla

def pedirAsignatura():
    return input("Introduce las asignaturas: ")

def mostrarAsignaturas():
    asignatura = tuple(pedirAsignatura() for i in range(4))
    print(", ".join(asignatura))
    
def main():
    borrarPantalla()
    mostrarAsignaturas()

if __name__ == "__main__":
    main()