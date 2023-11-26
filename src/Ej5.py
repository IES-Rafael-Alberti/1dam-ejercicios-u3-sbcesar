"""
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
"""

from borrarPantalla import borrarPantalla

def mostraListaInversa():
    lista = list(range(1,11))
    copia = lista.copy()
    copia.reverse()
    print(", ".join(map(str, copia)))

def main():
    borrarPantalla()

    mostraListaInversa()

    

if __name__ == "__main__":
    main()