"""
Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
"""

#cadena = hola:hello,nombre:name,es:is
#frase = hola mi nombre es cesar

from borrarPantalla import borrarPantalla

def introducirPalabras():
    return input("Introduce las palabras del diccionario (<palabra>:<traduccion>,<palabra>:<traduccion>,...): ")


def introducirFrase():
    return input("Introduce la frase que deseas traducir: ")


def formateoPalabras(cadena: str,palabraSpanish:list , palabraEnglish: list):
    listaTraducciones = cadena.split(",")

    for conjunto in listaTraducciones:
        palabra = conjunto.split(":")

        palabraSpanish.append(palabra[0])
        palabraEnglish.append(palabra[1])
    

def traductor(palabraSpanish: list, palabraEnglish:list, frase: str):
    fraseNueva = []

    #Obtiene el indice de la palabra en español ya que está en la misma posición que en su traduccion al inglés
    for palabra in frase.split(" "):
        if palabra in palabraSpanish:
            indice = palabraSpanish.index(palabra)
            fraseNueva.append(palabraEnglish[indice])    
        else:
            fraseNueva.append(palabra)
    
    palabraTraducida = " ".join(fraseNueva)

    print("Frase sin traducir: ", frase)
    print("Traducción: ", palabraTraducida)


def main():
    borrarPantalla()

    palabraSpanish = []
    palabraEnglish = []

    cadena = introducirPalabras()
    frase = introducirFrase()

    formateoPalabras(cadena, palabraSpanish, palabraEnglish)
    traductor(palabraSpanish, palabraEnglish, frase)
    

if __name__ == "__main__":
    main()