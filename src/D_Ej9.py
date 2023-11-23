"""
Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
"""

from borrarPantalla import borrarPantalla

def menu(facturas: dict):
    numFactura = 0
    coste = 0.0

    while True:
        menu = int(input("Introduce una opción:\n 1. Añadir factura.\n 2. Pagar factura.\n 3. Terminar\n"))

        match menu:
            case 1:
                numFactura += 1
                coste = pedirCosteFactura()
                agregarFactura(numFactura,coste,facturas)
                print()
            case 2:
                pagarFactura(facturas)
                print()
            case 3:
                break
            case _:
                print("Introduce una de las opciones disponibles (1, 2, 3)")

def pedirCosteFactura():
    return float(input("Introduce el coste de la factura: "))

def agregarFactura(numFactura: int, coste: float, facturas: dict):
    facturas[numFactura] = coste
    print("Factura agregada correctamente")
    print("Factura: ", facturas)

def pagarFactura(facturas: dict):
    print(facturas)
    facturaPagada = int(input("Introduce el número de la factura que desea borrar: "))

    if facturaPagada in facturas.keys():
        costoPagado = facturas[facturaPagada]
        del facturas[facturaPagada]
        print(f"La factura {facturaPagada}con coste {costoPagado} ha sido pagada correctamente")
    else:
        print(f"La factura {facturaPagada} no existe")
    print(facturas)

def main():
    borrarPantalla()
    facturas = {}
    menu(facturas)


if __name__ == "__main__":
    main()