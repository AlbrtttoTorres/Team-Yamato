# funciones.py
import numpy as np
from variables import DIMENSIONES, CARACTER_AGUA, CARACTER_BARCO, CARACTER_IMPACTO, CARACTER_FALLO

def generar_coordenadas_aleatorias():
    """
    Genera y devuelve una coordenada aleatoria (x, y) dentro de los límites del tablero.
    """
    x = np.random.randint(0, DIMENSIONES)
    y = np.random.randint(0, DIMENSIONES)
    return x, y

def colocar_barco(tablero, eslora):
    """
    Coloca un barco de longitud 'eslora' en el tablero de forma aleatoria.
    Se asegura de que el barco no salga del tablero ni se superponga con otro barco.
    """
    while True:
        orientacion = np.random.choice(['H', 'V'])  # Horizontal o Vertical
        x, y = generar_coordenadas_aleatorias()

        if orientacion == 'H' and y + eslora <= DIMENSIONES:
            # Comprobamos que no haya barcos en el área seleccionada
            if np.all(tablero[x, y:y+eslora] == CARACTER_AGUA):
                tablero[x, y:y+eslora] = CARACTER_BARCO
                return True
        elif orientacion == 'V' and x + eslora <= DIMENSIONES:
            # Comprobamos que no haya barcos en el área seleccionada
            if np.all(tablero[x:x+eslora, y] == CARACTER_AGUA):
                tablero[x:x+eslora, y] = CARACTER_BARCO
                return True

def inicializar_barcos(tablero, barcos):
    """
    Inicializa todos los barcos en el tablero dado.
    'barcos' es un diccionario con el tipo de barco y su eslora.
    """
    for tipo, eslora in barcos.items():
        for _ in range(barcos[tipo]):
            colocar_barco(tablero, eslora)

def imprimir_tablero(tablero, visible=False):
    """
    Imprime el tablero en un formato de cuadrícula en la consola.
    - `tablero`: El tablero a imprimir (array de numpy).
    - `visible`: Si es True, oculta la ubicación de los barcos que no han sido impactados.
    """
    print("   " + " ".join(str(i) for i in range(DIMENSIONES)))  
    print("  " + "-" * (DIMENSIONES * 2))  # Separador de cabecera
    for i in range(DIMENSIONES):
        # Fila con índices y contenido del tablero
        fila = []
        for j in range(DIMENSIONES):
            # Mostrar solo los impactos y fallos si el tablero es el visible del jugador
            if visible and tablero[i, j] == CARACTER_BARCO:
                fila.append(CARACTER_AGUA)  
            else:
                fila.append(tablero[i, j])  
        print(f"{i} | " + " ".join(fila))
    print()  # Línea de separación

def obtener_coordenadas_usuario():
    """
    Solicita al usuario una coordenada para disparar y la valida.
    """
    while True:
        try:
            x, y = map(int, input("Introduce las coordenadas de disparo (x y): ").split())
            if 0 <= x < DIMENSIONES and 0 <= y < DIMENSIONES:
                return x, y
            else:
                print(f"Por favor, introduce coordenadas dentro del rango (0-{DIMENSIONES-1}).")
        except ValueError:
            print("Entrada inválida. Introduce dos números separados por un espacio.")
