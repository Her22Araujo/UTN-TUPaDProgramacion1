tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
jugador = "X"
for turno in range(9):
    print("\nTablero:")
    for fila in tablero:
        print("  ".join(fila))
    columna = int(input(f"Jugador {jugador}, ingrese la columna (0-2): "))
    fila = int(input(f"\nJugador {jugador}, ingrese la fila (0-2): "))
    if 0 <= fila <= 2 and 0 <= columna <= 2:
        if tablero[fila][columna] == "-":
            tablero[fila][columna] = jugador

    
            if jugador == "X":
                jugador = "O"
            else:
                jugador = "X"
        else:
            print("Casilla llena")
    else:
        print("Cordenada invalida")


print("\nTablero final:")
for fila in tablero:
    print("".join(fila))