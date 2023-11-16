"""
Escribir un programa que almacene las matrices A=(123456) y B=(-100111) en una lista y muestre por pantalla su producto.
Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
"""

from borrarPantalla import borrarPantalla

def productoLista(A, B):
    return tuple(A[i] * B[i] for i in range(len(A)))

def producto(A, B):
    return tuple(productoLista(A[i], B[i]) for i in range(len(A)))

def main():
    borrarPantalla()
    A = [(1,2),(3,4),(5,6)]
    B = [(-1,0),(0,1),(1,1)]
    print(producto(A,B))

if __name__ == "__main__":
    main()