"""
Dadas las siguientes listas:

frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]

Crea conjuntos a partir de estas listas y nómbralos set_frutas1 y set_frutas2.
Encuentra las frutas que están en ambas listas y guárdalas en un nuevo conjunto llamado frutas_comunes.
Encuentra las frutas que están en frutas1 pero no en frutas2 y guárdalas en un conjunto llamado frutas_solo_en_frutas1.
Encuentra las frutas que están en frutas2 pero no en frutas1 y guárdalas en un conjunto llamado frutas_solo_en_frutas2.
"""

from borrarPantalla import borrarPantalla

def imprimirConjunto(conjunto):
    return ", ".join(conjunto)

def ambasListas(set_frutas1: set, set_frutas2: set):
    frutas_comunes = set_frutas1 & set_frutas2
    print("Frutas comunes: ", imprimirConjunto(frutas_comunes))
    

def frutasSoloFrutas1(set_frutas1: set, set_frutas2: set):
    frutas_solo_en_frutas1 = set_frutas1 - set_frutas2
    print("Frutas que están en frutas1 pero no en frutas2: ", imprimirConjunto(frutas_solo_en_frutas1))
    

def frutasSoloFrutas2(set_frutas1: set, set_frutas2: set):
    frutas_solo_en_frutas2 = set_frutas2 - set_frutas1
    print("Frutas que están en frutas2 pero no en frutas1: ", imprimirConjunto(frutas_solo_en_frutas2))
    

def main():
    borrarPantalla()

    frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
    frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]

    set_frutas1 = set(frutas1)
    set_frutas2 = set(frutas2)

    ambasListas(set_frutas1, set_frutas2)
    frutasSoloFrutas1(set_frutas1, set_frutas2)
    frutasSoloFrutas2(set_frutas1, set_frutas2)
    

if __name__ == "__main__":
    main()