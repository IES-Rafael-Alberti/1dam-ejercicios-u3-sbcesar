"""
Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de una escuela, finalizando cuando se introduzca “x”. A continuación, solicitar que introduzca los nombres de los alumnos de secundaria, finalizando al introducir “x”.

Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
Mostrar si todos los nombres de primaria están incluidos en secundaria.
"""

from borrarPantalla import borrarPantalla

def pedirNombrePrimaria(nombresPrimaria: set):
    while True:
        nombre = input("Introduce el nombre de pila de los alumnos de primaria ('x' para finalizar): ")
        if nombre.lower() == 'x':
            break
        nombresPrimaria.add(nombre)
    return nombresPrimaria

def pedirNombreSecundaria(nombresSecundaria: set):
    while True:
        nombre = input("Introduce el nombre de pila de los alumnos de secundaria ('x' para finalizar): ")
        if nombre.lower() == 'x':
            break
        nombresSecundaria.add(nombre)
    return nombresSecundaria

def mostrarAlumnosSinRepeticiones(nombresPrimaria: set, nombresSecundaria: set):
    print("Alumnos de primaria: ", pedirNombrePrimaria(nombresPrimaria))
    print("Alumnos de secundaria: ", pedirNombreSecundaria(nombresSecundaria))

def mostrarAlumnosRepetidos(nombresPrimaria: set, nombresSecundaria: set):
    alumnosRepetidos = nombresPrimaria & nombresSecundaria
    print("Los alumnos repetidores son: ", alumnosRepetidos)

def mostrarNoRepetidosSecundaria(nombresPrimaria: set, nombresSecundaria: set):
    noRepetidos = nombresPrimaria - nombresSecundaria
    print("Los alumnos de primaria que no se repiten en secundaria son: ", noRepetidos)

def incluidosSecundaria(nombresPrimaria: set, nombresSecundaria: set):
    todosIncluidos = nombresPrimaria.issubset(nombresSecundaria)
    print("¿Todos los nombres de primaria están incluidos en secundaria? ", todosIncluidos)

def main():
    borrarPantalla()

    nombresPrimaria = set()
    nombresSecundaria = set()

    mostrarAlumnosSinRepeticiones(nombresPrimaria, nombresSecundaria)
    mostrarAlumnosRepetidos(nombresPrimaria, nombresSecundaria)
    mostrarNoRepetidosSecundaria(nombresPrimaria, nombresSecundaria)
    incluidosSecundaria(nombresPrimaria, nombresSecundaria)

    

    

if __name__ == "__main__":
    main()