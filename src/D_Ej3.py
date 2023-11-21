"""
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta,
un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta.
Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
"""

from borrarPantalla import borrarPantalla

def preguntarFruta():
    return input("Introduce una fruta: ")

def preguntarKg():
    return float(input("Introduce los kg: "))

def calcularPrecioKg(fruteria,fruta):
    if fruta in fruteria:
        kg = preguntarKg()
        coste = fruteria[fruta] * kg
    else:
        raise KeyError("*** Error *** No tenemos esa fruta en la frutería")
    return coste

def main():
    borrarPantalla()

    fruteria = {"platano":1.35,"manzana":0.80,"pera":0.85,"naranja":0.70}

    fruta = preguntarFruta()
    

    try:
        print(calcularPrecioKg(fruteria,fruta))
    except KeyError as e:
        print(e)

if __name__ == "__main__":
    main()