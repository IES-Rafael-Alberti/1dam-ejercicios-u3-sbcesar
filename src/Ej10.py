"""
Escribir un programa que almacene en una lista los siguientes precios: 50, 75, 46, 22, 80, 65, 8 y muestre por pantalla el menor y el mayor de los precios.
"""

from borrarPantalla import borrarPantalla

def ordenar(precios:list):
    precios.sort()
    min = precios[0]
    max = precios[-1]
    return min,max

def main():
    borrarPantalla()
    precios = [50,75,46,22,80,65,8]
    print(ordenar(precios))
    
if __name__ == "__main__":
    main()