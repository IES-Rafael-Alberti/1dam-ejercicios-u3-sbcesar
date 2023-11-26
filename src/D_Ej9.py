"""
Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
"""

from borrarPantalla import borrarPantalla

def menu(facturas: dict):
    cantidadCobrada = 0
    while True:
        print("Cantidad cobrada hasta el momento: ", cantidadCobrada)
        print("Cantidad pendiente de cobro: ", sum(facturas.values()))

        opcion = int(input("Introduce una opción:\n 1. Añadir factura.\n 2. Pagar factura.\n 3. Terminar\n"))

        match opcion:
            case 1:
                agregarFactura(facturas)
                print()
            case 2:
                cantidadCobrada += pagarFactura(facturas)
                print()
            case 3:
                break
            case _:
                print("Introduce una de las opciones disponibles (1, 2, 3)")

def pedirCosteFactura():
    while True:
        try:
            return float(input("Introduce el coste de la factura: "))
        except ValueError:
            print("Por favor ingrese un valor numérico.")

def agregarFactura(facturas: dict):
    numFactura = len(facturas) + 1
    coste = pedirCosteFactura()
    facturas[numFactura] = coste
    print("Factura agregada correctamente")
    return coste

def pagarFactura(facturas: dict):
    print("Facturas: ", facturas)
    facturaPagada = int(input("Introduce el número de la factura que desea borrar: "))

    if facturaPagada in facturas:
        cantidadCobrada = facturas.pop(facturaPagada)
        print(f"La factura {facturaPagada}con coste {cantidadCobrada} ha sido pagada correctamente")
        return cantidadCobrada
    else:
        print(f"La factura {facturaPagada} no existe")
        return 0

def main():
    borrarPantalla()
    facturas = {}
    menu(facturas)


if __name__ == "__main__":
    main()