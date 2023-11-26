"""
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
"""

from borrarPantalla import borrarPantalla

def preguntarDivisa() -> str:
    return input("Dime que divisa quieres mostrar: ")

def mostrarDivisa(monedas: dict):
    divisa = preguntarDivisa()
    
    if divisa in monedas:
        return monedas[divisa]
    else:
        raise KeyError(" *** Error *** - La divisa no esta en el diccionario")

def main():
    borrarPantalla()

    monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

    try:
        print(mostrarDivisa(monedas))
    except KeyError as e:
        print(e)

if __name__ == "__main__":
    main()