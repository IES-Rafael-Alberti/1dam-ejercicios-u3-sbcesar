"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje
En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las 
correspondientes notas introducidas por el usuario.
"""

from borrarPantalla import borrarPantalla

def listaNotas(asignaturas):
    return list(float(input(f"Introduce tu nota de {asignatura}: ")) for asignatura in asignaturas)

def mostrarAsigNota(asignaturas, notas):
    for i in range(0, len(asignaturas)):
        print(f"En {asignaturas[i]} has sacado {notas[i]}")
    
def main():
    borrarPantalla()
    
    asignaturas = ["Mates","Lengua","Fisica"]
    notas = listaNotas(asignaturas)
    mostrarAsigNota(asignaturas,notas)


if __name__ == "__main__":
    main()