"""
Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

Lista de la compra
-----------------------
Articulo1       Precio
Articulo2       Precio
ArticuloN       Precio
-----------------------
Total           Coste
"""

from borrarPantalla import borrarPantalla

def agregarCompra(listaCompra: dict):
    while True:
        articulo = input("Introduce un artículo: ")

        if not articulo:                    #Si no introduce nada se sale del bucle y termina
            break

        if articulo in listaCompra:         #Si ya está en el diccionario ignora el valor introducido y vuelve a preguntar
            print(f"El {articulo} ya está en la lista de la compra, por favor añade otro artículo.")
            continue

        precio = float(input("Introduce el precio del artículo: "))
        listaCompra[articulo] = precio      #Añade el artículo y su precio al diccionario

    return listaCompra

def calcularPrecio(listaCompra: dict):
    cont = 0
    for i in listaCompra.values():
        cont += i
    return cont

def mostrarListaCompra(listaCompra: dict):
    agregar = agregarCompra(listaCompra)
    header = "Lista de la compra"
    print(header)
    print("-" * len(header))
    
    for articulo, precio in listaCompra.items():
        print(f"{articulo}       {precio}")

    print("-" * len(header))
    print(f"Lista de la compra: {listaCompra}       Precio total: {calcularPrecio(listaCompra)}")



def main():
    borrarPantalla()

    listaCompra = {}
    
    mostrarListaCompra(listaCompra)
    

if __name__ == "__main__":
    main()