"""
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
"""

from borrarPantalla import borrarPantalla

def productoEscalar(vector1:list,vector2:list):
    vector3 = []
    for i in range(len(vector1)):
        solucion = vector1[i] * vector2[i]
        vector3.append(solucion)
    return vector3

def main():
    borrarPantalla()
    
    vector1 = [1,2,3]
    vector2 = [-1,0,2]
    
    print(f"El producto escalar de {vector1} y {vector2} es {productoEscalar(vector1,vector2)}")

if __name__ == "__main__":
    main()