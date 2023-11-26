"""
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
"""

from borrarPantalla import borrarPantalla

def preguntarNombre() -> str:
    return input("Introduce tu nombre: ")

def preguntarEdad() -> int:
    return input("Introduce tu edad: ")

def preguntarDireccion() -> str:
    return input("Introduce tu direccion: ")
 
def preguntarTelefono() -> int:
    return input("Introduce tu numero de telefono: ")

def crearDiccionario(info: dict, nombre: str, edad: int, direccion: str, tlf: int):
    info.setdefault("Nombre", nombre)
    info.setdefault("Edad", edad)
    info.setdefault("Direccion", direccion)
    info.setdefault("Telefono", tlf)

def mostrarInfo(info: dict):
    return f"{info['Nombre']} tiene {info['Edad']} años, vive en {info['Direccion']} y su numero de telefono es {info['Telefono']}."

def main():
    borrarPantalla()

    info = {}
    nombre = preguntarNombre()
    edad = preguntarEdad()
    direccion = preguntarDireccion()
    tlf = preguntarTelefono()

    crearDiccionario(info, nombre, edad, direccion, tlf)
    print(mostrarInfo(info))



if __name__ == "__main__":
    main()