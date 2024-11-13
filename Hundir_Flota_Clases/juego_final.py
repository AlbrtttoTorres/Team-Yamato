# main.py
import numpy as np
from tablero import Tablero
from funciones import generar_coordenadas_aleatorias, imprimir_tablero
from variables import DIMENSIONES
from variables import BARCOS

def main():
    print("¡Bienvenido a Hundir la Flota!")
    print("Instrucciones: Intenta hundir todos los barcos de la máquina antes de que hundan los tuyos.")
    
    # Inicializar tableros de jugador y máquina
    tablero_jugador = Tablero(id_jugador="jugador")
    tablero_maquina = Tablero(id_jugador="máquina")

    juego_terminado = False
    turno_jugador = True  

    while not juego_terminado:
        if turno_jugador:
            print("\nTu tablero de disparos:")
            imprimir_tablero(tablero_maquina.tablero_visible)
            x, y = map(int, input("Introduce las coordenadas de disparo (x y): ").split())
            
            if tablero_maquina.recibir_disparo(x, y):
                print("¡Impacto! Vuelve a disparar.")
            else:
                print("Agua... le toca a la máquina.")
                turno_jugador = False
        else:
            x, y = generar_coordenadas_aleatorias()
            print(f"La máquina dispara a ({x}, {y})...")
            
            if tablero_jugador.recibir_disparo(x, y):
                print("¡La máquina te ha dado! Vuelve a disparar.")
            else:
                print("La máquina falló... ¡Tu turno!")
                turno_jugador = True
            
        # Comprobación de fin de juego
        if tablero_maquina.barcos_restantes() == 0:
            print("¡Felicidades! Has hundido todos los barcos enemigos. ¡Ganaste!")
            juego_terminado = True
        elif tablero_jugador.barcos_restantes() == 0:
            print("La máquina ha hundido todos tus barcos. Has perdido.")
            juego_terminado = True

if __name__ == "__main__":
    main()
