"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
"""

from borrarPantalla import borrarPantalla

def pedirpalabra():
    palabra = input("Introduce una palabra: ").strip().lower()
    palabra = palabra.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    return input("Introduce una palabra: ")

def contarVocal(palabra: str,vocales: list):
    for vocal in vocales:
        vocal[1] = palabra.count(vocal[0])
    return vocales
        
def main():
    borrarPantalla()
    vocales = [["a",0],["e",0],["i",0],["o",0],["u",0]]
    palabra = pedirpalabra()
    print(contarVocal(palabra,vocales))
    
if __name__ == "__main__":
    main()