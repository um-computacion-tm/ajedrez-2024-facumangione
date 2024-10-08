from .chess import Chess
from .exceptions import InvalidMove, OutOfBoundsError, NonNumericInputError, GameOverException, NonPieceOriginError, WrongTurnError, InvalidPieceMoveError

# Función principal del programa
def start_game():
    partida = Chess()
    while True:
        try:
            run_game(partida)
        except GameOverException as game_end:
            print(str(game_end))
            print("Juego terminado.")
            break  # Sale del bucle para finalizar el juego

# Muestra el tablero con íconos de piezas
def render_board_with_icons(tablero):   
    piezas_icons = {
        'R': '♜', 'N': '♞', 'B': '♝', 'Q': '♛', 'K': '♚', 'P': '♟',
        'r': '♖', 'n': '♘', 'b': '♗', 'q': '♕', 'k': '♔', 'p': '♙',
        '.': '·'  # Casilla vacía
    }
    for fila in tablero:
        print(' '.join(piezas_icons.get(pieza, '.') for pieza in fila))

# Lógica del juego de ajedrez
def run_game(partida):
    try:
        render_board_with_icons(partida.get_board())
        print("Indica las coordenadas de la pieza que quieres mover y su destino.")
        print("Escribe EXIT para finalizar la partida.")
        print("Turno actual:", partida.turno)

        # Solicitar coordenadas en un bucle
        origen_fila = obtener_input("Fila de origen: ")
        origen_columna = obtener_input("Columna de origen: ")
        destino_fila = obtener_input("Fila de destino: ")
        destino_columna = obtener_input("Columna de destino: ")

        # Validar y convertir las coordenadas
        origen_fila, origen_columna, destino_fila, destino_columna = map(int, [origen_fila, origen_columna, destino_fila, destino_columna])

        # Ejecutar el movimiento de la pieza
        partida.realizar_movimiento(origen_fila, origen_columna, destino_fila, destino_columna)

        # Verificar si exit fue invocado
        print("DEBUG: Movement completed, checking for next input.")
        
    except (InvalidMove, NonPieceOriginError, WrongTurnError, InvalidPieceMoveError) as error:
        print("Movimiento inválido:", error)

# Función para obtener la entrada del usuario
def obtener_input(prompt):
    while True:
        valor = input(prompt)
        if valor.upper() == "EXIT":
            print("Juego terminado.")
            exit()  # Esto llama a exit
        if valor.isdigit() and 0 <= int(valor) < 8:
            return valor
        print("Entrada inválida. Por favor ingresa un número entre 0 y 7.")


if __name__ == "__main__":
    start_game()