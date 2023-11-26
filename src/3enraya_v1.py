import os

#Simbolos que se mostrarán en el tablero
FICHAS = (" ","X","O")

def borrarConsola():
    """Limpiar la consola"""

    os.system("cls")

def pulsarTeclaParaContinuar():
    """Mostrar el mensaje Presione una tecla para continuar y
    hacer una pausa hasta que se realice la accion"""

    os.system("pause")

def crearFila(numColumnas = 3) -> list:
    """Crear las columnas de una fila"""

    return list(0 for _ in range(numColumnas))

def mostrarFila(fila: list):
    """Mostrar una fila del tablero"""

    contenidoFila = "| "
    for celda in fila:
        contenidoFila += FICHAS[celda] + " | "
    print(contenidoFila)

def crearTablero(numFilas = 3) -> tuple:    #por defecto 3
    """Crear el tablero 3x3"""

    return tuple(crearFila() for _ in range(numFilas))

def mostrarTablero(tablero: tuple):
    """Mostrar en consola el tablero con las fichas"""

    borrarConsola()
    print("-" * 13)
    for fila in tablero:
        mostrarFila(fila)
        print("-" * 13)

def cambiarTurno(turno: int) -> int:
    """Modifica el turno"""

    if turno % 2 == 0:
        return 1
    return 2

def pedirPosicion(fila_col: str, msg: str = "") -> int:
    pos  = None
    if msg != "": print(msg)
    while pos == None:
        try:
            pos = int(input(f"Elige la {fila_col} (1, 2, 3): ")) - 1
            if not 0 <= pos <= 2:
                raise ValueError
        except ValueError:
            pos = None
            print(f"***Error*** {fila_col} no válida")

def comprobarCasilla(tablero: tuple, posFicha: dict) -> bool:
    """Comprueba si la casilla seleccionada es correcta para colocar la ficha del jugador"""

    return tablero[posFicha["fila"]][posFicha] == 0

def colocarFicha(tablero: tuple, jugador: int):
    """Solicita al jugador la posicion de las fichas que va a colocar"""

    posFicha = {"fila":None, "columna": None}
    posCorrecto = False

    while not posCorrecto:
        posFicha["fila"] = pedirPosicion("fila", f"\nJugador {jugador}, coloque una ficha...")
        posFicha["columna"] = pedirPosicion("columna")

        posCorrecto = comprobarCasilla(tablero, posFicha)

        if posCorrecto:
            tablero[posFicha["fila"]][posFicha["columna"]] = jugador
        else:
            [posFicha["fila"]] = [posFicha["columna"]] = None
            print("*** Error ***  - Movimiento inválido")
            pulsarTeclaParaContinuar()
            mostrarTablero(tablero)

def verificarGanador(tablero) -> tuple:
    """Comprobar si el ganador ha colocado bien las fichas"""
    return tablero


def jugar(tablero: tuple):

    turno = 0
    ronda = 0
    hayGanador = False

    while not hayGanador:
        turno = cambiarTurno(turno)
        if turno == 1:
            ronda += 1
        
        print(f"\nRONDA {ronda}")
        print(f"_" * len(f"RONDA {ronda}") + "\n")

        print(turno)

        colocarFicha()
        mostrarTablero(tablero)

        if ronda <= 3:
            ganador, hayGanador = verificarGanador(tablero)
        
        if hayGanador:
            print(f"\n¡El jugador {ganador} ha ganado!\n")
        
        if ronda == 9:
            hayGanador = True
            print("\n¡Empate!\n")





def main():
    tablero = crearTablero()
    mostrarTablero(tablero)
    jugar(tablero)
    

if __name__ == "__main__":
    main()