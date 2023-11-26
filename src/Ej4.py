"""
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y
los muestre por pantalla ordenados de menor a mayor.
"""

from borrarPantalla import borrarPantalla

def pedirNumGanador() -> int:
    return int(input("Introduce los numeros ganadores de la loteria primitiva: "))

def listaPrimitiva():
    numerosGanadores = list(pedirNumGanador() for i in range(5))
    numerosGanadores.sort()
    return numerosGanadores

def main():
    borrarPantalla()

    print(listaPrimitiva())

if __name__ == "__main__":
    main()