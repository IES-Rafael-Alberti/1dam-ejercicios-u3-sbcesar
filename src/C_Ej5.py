"""
Dado el conjunto de números enteros:

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

Crea un conjunto pares que contenga los números pares del conjunto numeros.
Crea un conjunto multiplos_de_tres que contenga los números que son múltiplos de tres del conjunto numeros.
Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y guárdala en un conjunto llamado pares_y_multiplos_de_tres.
"""
from borrarPantalla import borrarPantalla

def imprimirConjunto(conjunto):
    return ", ".join(map(str, sorted(conjunto)))

def conjuntoPares(numeros: set):
    conjuntoPares = set()

    for num in numeros:
        if num % 2 == 0:
            conjuntoPares.add(num)

    return conjuntoPares

def multiplosDeTres(numeros: set):
    multiplos_de_tres = set()
    
    for num in numeros:
        if num % 3 == 0:
            multiplos_de_tres.add(num)
    
    return multiplos_de_tres

def paresMultiplosDeTres(conjuntoPares: set, multiplosDeTres: set):
    pares_y_multiplos_de_tres = conjuntoPares & multiplosDeTres
    print("La intersección entre los conjuntos pares y multiplos_de_tres son: ", imprimirConjunto(pares_y_multiplos_de_tres))


def main():
    borrarPantalla()

    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    conjunto_pares = conjuntoPares(numeros)
    multiplos_de_tres = multiplosDeTres(numeros)

    print("Conjunto de pares: ", imprimirConjunto(conjunto_pares))
    print("Conjunto de múltiplos de tres: ", imprimirConjunto(multiplos_de_tres))
    paresMultiplosDeTres(conjunto_pares, multiplos_de_tres)

if __name__ == "__main__":
    main()