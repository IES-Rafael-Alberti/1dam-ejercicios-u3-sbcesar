"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
"""

from borrarPantalla import borrarPantalla

def pedirPalabra():
    return list(input("Introduce una palabra: "))

def comparar(palabra: list):
    palabra2 = palabra.copy()
    palabra2.reverse()
    if palabra == palabra2:
        return palabra

def main():
    borrarPantalla()
    palabra = pedirPalabra()
    print(comparar(palabra))

if __name__ == "__main__":
    main()