"""
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""

from borrarPantalla import borrarPantalla

"""
    - diccionario.setdefault("":"") --> si ya está en el diccionario ignora el valor proporcionado
    - diccionario[clave] = valor    --> si ya está en el diccionario sobreescribe el valor proporcionado
"""

def mostrarInfo(d: dict):
    while True:
        clave = input("Introduce lo que quieras mostrar: ")
        valor = input(f"Introduce tu {clave}: ")
        if clave == "" or valor == "":
            break
        d.setdefault(clave,valor)
        print(d)
        
def main():
    borrarPantalla()

    d = {}
    mostrarInfo(d)
    
if __name__ == "__main__":
    main()

"""
CÓDIGO MEJORADO
def mostrar_info(d: dict):
    while True:
        clave = input("Introduce lo que quieras agregar (o presiona Enter para terminar): ")
        if not clave:
            break

        if clave in d:
            print(f"La clave '{clave}' ya existe. Introduce una clave diferente.")
            continue

        valor = input(f"Introduce tu {clave}: ")
        d[clave] = valor
        print("Contenido del diccionario:")
        for key, value in d.items():
            print(f"{key}: {value}")
"""