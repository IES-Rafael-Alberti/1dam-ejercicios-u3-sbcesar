"""
Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
"""

#hola:hello,nombre:name,es:is

from borrarPantalla import borrarPantalla

def introducirPalabras():
    return input("Introduce las palabras del diccionario (<palabra>:<traduccion>,<palabra>:<traduccion>,...): ")

def formateoPalabras(palabra: str):
    listaTraducciones = palabra.split(",")
    
    for palabra in listaTraducciones:
        palabraIngles = palabra 

def main():
    borrarPantalla()

    palabra = introducirPalabras()
    print(formateoPalabras(palabra))
    

if __name__ == "__main__":
    main()