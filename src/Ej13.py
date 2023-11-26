"""
Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y
muestre por pantalla su media y desviación típica.
"""
import statistics
from borrarPantalla import borrarPantalla

def pedirNumeros() -> str:
    return input("introduce una serie de numeros separados por comas: ")

def guardarLista(numeros: str):
    return list(numeros.split(","))

def media(lista):
    cantNumeros = len(lista)
    suma = 0
    for numero in lista:
        suma += int(numero)
    media = suma / cantNumeros
    return media

def desviacionTipica(lista):
    lista2 = [int(i) for i in lista]
    desviacionTipica = statistics.stdev(lista2)
    return desviacionTipica

def main():
    borrarPantalla()
    numeros = pedirNumeros()
    lista = guardarLista(numeros)
    print("La media es: ", media(lista))
    print("La desviacion tipica es: ", desviacionTipica(lista))

if __name__ == "__main__":
    main()

#1,2,34,4,6