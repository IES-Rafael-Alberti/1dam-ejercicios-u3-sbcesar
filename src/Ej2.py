"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y
la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> sobre cada una de las asignaturas de la lista.
"""

from borrarPantalla import borrarPantalla

def pedirAsignaturas():
    return input("Introduce las asignaturas: ")

def mostrarAsignaturas():
    asignatura = tuple(pedirAsignaturas() for i in range(4))
    for i in asignatura:
        print("Yo estudio ", i)

def main():
    borrarPantalla()
    mostrarAsignaturas()


if __name__ == "__main__":
    main()