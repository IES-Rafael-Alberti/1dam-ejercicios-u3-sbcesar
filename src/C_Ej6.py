"""
Dado el conjunto de letras:

vocales = {'a', 'e', 'i', 'o', 'u'}

Crea un conjunto consonantes que contenga las letras del alfabeto que no son vocales.
Crea un conjunto letras_comunes que contenga las letras que están tanto en el conjunto vocales como en el conjunto consonantes.
"""

import string
from borrarPantalla import borrarPantalla

def imprimirConjunto(conjunto):
    return ", ".join(map(str, conjunto))

def consonantes(vocales: set, abecedario: set) -> set:
    consonantes = abecedario - vocales
    consonantes = sorted(consonantes)
    return consonantes

def letrasComunes(vocales:set, consonantes: set) -> set:
    letras_comunes = vocales.intersection(consonantes)
    return letras_comunes

def main():
    borrarPantalla()

    vocales = {'a', 'e', 'i', 'o', 'u'}
    abecedario = set(string.ascii_lowercase)
    conjuntoConsonantes = consonantes(vocales, abecedario)
    conjuntoLetrasComunes = letrasComunes(vocales, conjuntoConsonantes)

    print("Las letras consonantes son: ", imprimirConjunto(conjuntoConsonantes))
    print("Las letras comunes entre el conjunto vocales y el conjunto consonantes son: ", imprimirConjunto(conjuntoLetrasComunes))

if __name__ == "__main__":
    main()