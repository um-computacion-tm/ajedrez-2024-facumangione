from chess import Chess
from exceptions import InvalidMove, OutOfBoundsError, NonNumericInputError, GameOverException

# Función principal del programa
def start_game():
    #La función start_game() es el punto de inicio del programa.
    partida = Chess()
    while True:
        try:
            run_game(partida)
        except GameOverException as game_end:
            print(str(game_end))
            exit()

# Muestra el tablero con íconos de piezas
def render_board_with_icons(tablero):
    #La función render_board_with_icons() muestra el tablero de ajedrez utilizando íconos para representar las piezas.
    # Mapeo de piezas a íconos
    piezas_icons = {
        'R': '♜', 'N': '♞', 'B': '♝', 'Q': '♛', 'K': '♚', 'P': '♟',
        'r': '♖', 'n': '♘', 'b': '♗', 'q': '♕', 'k': '♔', 'p': '♙',
        '.': '·'  # Casilla vacía
    }
    # Reemplazar letras por íconos
    for fila in tablero:
        print(' '.join(piezas_icons[pieza] for pieza in fila))

# Lógica del juego de ajedrez
def run_game(partida):
    #La función run_game() gestiona los movimientos durante una partida de ajedrez.
    try:
        # Mostrar el tablero y el turno actual, luego solicitar coordenadas
        render_board_with_icons(partida.get_board())
        print("Indica las coordenadas de la pieza que quieres mover y su destino.")
        print("Escribe EXIT para finalizar la partida.")
        print("Turno actual:", partida.turn)
        
        origen_fila = input("Fila de origen: ")
        if origen_fila.upper() == "EXIT":
            print("Juego terminado.")
            exit()
        
        origen_columna = input("Columna de origen: ")
        if origen_columna.upper() == "EXIT":
            print("Juego terminado.")
            exit()

        destino_fila = input("Fila de destino: ")
        if destino_fila.upper() == "EXIT":
            print("Juego terminado.")
            exit()

        destino_columna = input("Columna de destino: ")
        if destino_columna.upper() == "EXIT":
            print("Juego terminado.")
            exit()

        # Validar que las entradas sean numéricas
        if not (origen_fila.isdigit() and origen_columna.isdigit() and destino_fila.isdigit() and destino_columna.isdigit()):
            raise NonNumericInputError()

        # Convertir las coordenadas a enteros
        origen_fila = int(origen_fila)
        origen_columna = int(origen_columna)
        destino_fila = int(destino_fila)
        destino_columna = int(destino_columna)

        # Validar que las coordenadas estén dentro del rango
        if not (0 <= origen_fila < 8 and 0 <= origen_columna < 8 and 0 <= destino_fila < 8 and 0 <= destino_columna < 8):
            raise OutOfBoundsError()

        # Ejecutar el movimiento de la pieza
        partida.move(origen_fila, origen_columna, destino_fila, destino_columna)

    except InvalidMove as error:
        print("Movimiento inválido:", error)

if __name__ == "__main__":
    start_game()
