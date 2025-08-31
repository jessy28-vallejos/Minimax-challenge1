import random

class Grilla: # Se crea la estructura de la grilla

    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.gato = (0, 0)
        self.raton = None
        self.grilla = [['.' for _ in range(columnas)] for _ in range(filas)]
        # Cuatro movimientos
        self.move = [(1,0),(-1,0),(0,1),(0,-1)]
        self.turnos = 0
        self.turnos_validos = 10

    # Posición aleatoria del ratón
    def posicion_raton(self):
        while True:
            x = random.randint(0, self.filas - 1)
            y = random.randint(0, self.columnas - 1)
            if (x, y) != self.gato:
                self.raton = (x, y)
                break

    # Refresca la grilla
    def actualizar_grilla(self):
        self.grilla = [['.' for _ in range(self.columnas)] for _ in range(self.filas)]
        self.grilla[self.raton[0]][self.raton[1]] = 'R'
        self.grilla[self.gato[0]][self.gato[1]] = 'G'

    # Minimax (ratón = MAX, gato = MIN) con heurística Manhattan simple
    def minimax(self, profundidad, es_raton, gato, raton, devolver_mov=False):
        
        #Distancia heuristica = distancia Manhattan
        def heuristica(pos_gato, pos_raton):
            return abs(pos_gato[0] - pos_raton[0]) + abs(pos_gato[1] - pos_raton[1])

        # Caso base: profundidad 0 o captura
        if profundidad == 0 or gato == raton:
            return heuristica(gato, raton), raton

        # Turno del ratón (MAX)
        if es_raton:
            mejor_val = float('-inf')
            mejor_mov = raton
            for pos_x, pos_y in self.move:
                nuevo_raton = (raton[0] + pos_x, raton[1] + pos_y)
                if 0 <= nuevo_raton[0] < self.filas and 0 <= nuevo_raton[1] < self.columnas:
                    val, _ = self.minimax(profundidad - 1, False, gato, nuevo_raton)
                    if val > mejor_val:
                        mejor_val = val
                        mejor_mov = nuevo_raton
            return (mejor_val, mejor_mov) if devolver_mov else (mejor_val, mejor_mov)

        # Turno del gato (MIN)
        else:
            mejor_val = float('inf')
            mejor_mov = gato
            for pos_x, pos_y in self.move:
                nuevo_gato = (gato[0] + pos_x, gato[1] + pos_y)
                if 0 <= nuevo_gato[0] < self.filas and 0 <= nuevo_gato[1] < self.columnas:
                    val, _ = self.minimax(profundidad - 1, True, nuevo_gato, raton)
                    if val < mejor_val:
                        mejor_val = val
                        mejor_mov = nuevo_gato
            return (mejor_val, mejor_mov)

# imprime tablero
def imprimir_laberinto(laberinto):
    for fila in laberinto:
        print('| ' + ' | '.join(fila) + ' |')
    print()

# movimientos válidos alrededor del ratón (para el primer turno random) y para el gato
def crear_posiciones(posicion, movimientos_validos, fila, columna):
    lista_posiciones = []
    for row, col in movimientos_validos:
        nuevo_x, nuevo_y = posicion[0] + row, posicion[1] + col
        if 0 <= nuevo_x < fila and 0 <= nuevo_y < columna:
            lista_posiciones.append((nuevo_x, nuevo_y))
    return lista_posiciones

# Funcion Principal
if __name__ == '__main__':
    random.seed()  # utiliza el tiempo del sistema, tiempo actual

    filas = 5
    columnas = 5
    profundidad_mm = 3          # (1=facil, 3=normal, 5=mas pensante)
    raton_random_turnos = 1     # el ratón se mueve al azar solo en el primer turno

    Laberinto = Grilla(filas, columnas) #se llama a la clase 
    Laberinto.posicion_raton() #se crean las posiciones dentro de la clase Laberinto
    Laberinto.actualizar_grilla() #se actualiza la grilla

    print('Estado inicial:')
    imprimir_laberinto(Laberinto.grilla) #se imprime la grilla inicial

    for turno in range(Laberinto.turnos_validos): #jugadas validas
        print(f'--- Turno {turno + 1} ---')

        # Movimiento del gato (usuario)
        posiciones = crear_posiciones(Laberinto.gato, Laberinto.move, Laberinto.filas, Laberinto.columnas) #se crean posiciones validas para el gato
        print(f'Posiciones válidas para el gato: {posiciones}')

        while True:
            try:
                x, y = map(int, input('Ingrese la jugada del gato (fila columna): ').split())
                if (x, y) in posiciones:
                    Laberinto.gato = (x, y)
                    break
                else:
                    print('Posición inválida. Elija una de las posiciones válidas.')
            except ValueError:
                print('Entrada inválida. Ingrese dos números separados por un espacio.')

        # Movimiento del ratón
        if turno < raton_random_turnos:
            # primer turno: movimiento al azar válido
            candidatos = crear_posiciones(Laberinto.raton, Laberinto.move, Laberinto.filas, Laberinto.columnas)
            if candidatos:
                Laberinto.raton = random.choice(candidatos) # se elije al azar posiciones para el raton
        else:
            # luego: minimax (ratón MAX) - devuelve mejor_distancia_heuristica y mejor_posicion_raton
            _, mejor_posicion_raton = Laberinto.minimax(profundidad_mm, True, Laberinto.gato, Laberinto.raton, devolver_mov=True)
            Laberinto.raton = mejor_posicion_raton # guarda en la grilla la nueva posicion del raton

        # ¿El gato atrapó al ratón? - termina el juego
        if Laberinto.gato == Laberinto.raton:
            print(f'El ratón se movió a {Laberinto.raton}')
            print('¡El ratón fue atrapado! Juego terminado.')
            Laberinto.actualizar_grilla()
            imprimir_laberinto(Laberinto.grilla)
            break

        print(f'Ratón se mueve a {Laberinto.raton}')
        print('Después del movimiento del ratón:')
        Laberinto.actualizar_grilla()
        imprimir_laberinto(Laberinto.grilla)
    else:
        print('Se agotaron los turnos sin que el gato atrape al ratón.')
