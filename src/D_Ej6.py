"""
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""

from borrarPantalla import borrarPantalla

def mostrarInfo(d: dict):
    clave = input("Introduce lo que quieras mostrar: ")
    valor = input(f"Introduce tu {clave}: ")

    while True:
        



def main():
    borrarPantalla()

    d = {}
    mostrarInfo(d)
    
    

if __name__ == "__main__":
    main()