====================================================================
                 JUEGO GATO Y RATÓN 
                 con Algoritmo Minimax
====================================================================

DESCRIPCIÓN
-------------
Juego por turnos donde un GATO (jugador) intenta atrapar un RATÓN (IA)
en una grilla 5x5. El ratón usa el algoritmo minimax para decisiones inteligentes.

OBJETIVO
----------
• GATO: Atrapar al ratón en 10 turnos o menos
• RATÓN: Sobrevivir 10 turnos completos

ALGORITMO MINIMAX
-------------------
• Profundidad: 3 niveles
• Heurística: Distancia Manhattan positiva
• Estrategia:
  - RATÓN (MAX): Maximiza distancia para escapar del gato
  - GATO (MIN): Minimiza distancia

CÓMO JUGAR
------------
1. Ejecutar: Challenge_one.py
2. TURNO GATO:
   - Se muestran posiciones válidas
   - Ingresar coordenadas: fila columna (ej: 2 3)
3. TURNO RATÓN: 
   - La IA mueve automáticamente
4. Gana quien cumpla su objetivo en 10 turnos

CONTROLES
-----------
• Movimiento en 4 direcciones
• Coordenadas: 0 a 4 (filas y columnas)
• Formato de entrada: "fila columna" (ej: 1 2)

ESTRUCTURA DEL CÓDIGO
-----------------------
Clase Grilla:
• __init__()       - Inicializa tablero
• posicion_raton() - Coloca ratón aleatorio
• actualizar_grilla() - Actualiza display
• minimax()        - Algoritmo de IA

Funciones:
• imprimir_laberinto()    - Muestra tablero
• crear_posiciones_gato() - Calcula movimientos válidos

TABLERO
---------
Símbolos:
• G = Gato (jugador)
• R = Ratón (IA)
• . = Celda vacía

Ejemplo:
| . | . | . | . | . |
| . | . | G | . | . |
| . | . | . | R | . |
| . | . | . | . | . |
| . | . | . | . | . |

ESTRATEGIAS
-------------
Para GATO:
• Moverse (Arriba, abajo, izquierda, derecha)
• Usar esquinas para limitar

Para RATÓN:
• Moverse (Arriba, abajo, izquierda, derecha)
• Mantener distancia máxima
• Evitar esquinas
• Moverse lejos del gato

EJECUCIÓN
-----------
Requisitos: Python 3.6+
Comando: Challenge_one.py

TURNOS
--------
• Máximo 10 turnos
• Juego termina si:
  - Gato atrapa ratón
  - Se completan 10 turnos

NOTAS TÉCNICAS
----------------
• Heurística: Distancia Manhattan
• Profundidad búsqueda: 3 niveles
• Validación de movimientos incluida
• Entrada usuario verificada

CONDICIONES DE VICTORIA
-------------------------
• VICTORIA GATO: Posiciones coinciden
• VICTORIA RATÓN: Sobrevive 10 turnos

====================================================================
                 ¡QUE COMIENCE LA CAZA! 🐭🏃💨🐱
====================================================================
