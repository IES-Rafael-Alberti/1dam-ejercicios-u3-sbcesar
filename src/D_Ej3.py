"""
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta,
un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta.
Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
"""

from borrarPantalla import borrarPantalla

def mostrarDiccionario():
    return ""

def main():
    try:
        print(mostrarDiccionario())
    except NameError as e:
        print(e)

if __name__ == "__main__":
    main()