"""
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha
en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
"""

from borrarPantalla import borrarPantalla

def preguntarFecha():
    return dict(input("Introduce una fecha (dd/mm/yyyy)"))

def cambioFormato(fecha:dict):
    return fecha

def main():
    borrarPantalla()

    fecha = preguntarFecha()

    

if __name__ == "__main__":
    main()