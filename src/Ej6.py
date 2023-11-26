"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""

from borrarPantalla import borrarPantalla

def pedirNota(asignaturas):
    cont = 0
    for i in range(len(asignaturas)):
        nota = float(input("Introduce la nota (0-10): "))
        asignaturas[cont][1] = nota
        cont += 1

def eliminar(asignaturas):
    for i in range(len(asignaturas) - 1, -1, -1):
        if asignaturas[i][1] >= 5:
            del asignaturas[i]
        
def main():
    borrarPantalla()
    
    asignaturas = [["Mates",0],["Lengua",0],["Fisica",0]]
    pedirNota(asignaturas)
    eliminar(asignaturas)
    print(asignaturas)

if __name__ == "__main__":
    main()