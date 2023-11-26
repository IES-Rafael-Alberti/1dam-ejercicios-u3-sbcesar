"""
Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
"""

from borrarPantalla import borrarPantalla

def creditosAsignaturas(asignaturas:dict):
    cont = 0
    for asignatura, creditos in asignaturas.items():
        print(f"{asignatura} tiene {creditos} créditos.")
        cont += creditos
    print(f"El número total de créditos del curso es de {cont}")

def main():
    borrarPantalla()

    asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    creditosAsignaturas(asignaturas)
    

if __name__ == "__main__":
    main()