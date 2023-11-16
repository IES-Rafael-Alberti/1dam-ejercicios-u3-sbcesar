"""
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3,
y muestre por pantalla la lista resultante.
"""

import string
from borrarPantalla import borrarPantalla

def eliminarMultiplos(lista) -> list:
    for i in range(0,len(lista), 3):
        if i == 0:
            i += 2
            lista.pop(i)
        elif i == lista[:-2]:
            return lista
        else:
            i += 3
            lista.pop(i)

def main():
    borrarPantalla()

    lista = list(string.ascii_lowercase)
    print(", ".join(lista))
    print(eliminarMultiplos(lista))




if __name__ == "__main__":
    main()