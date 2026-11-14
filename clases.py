import random
import numpy as nd



class Tablero:
    """
    Tablero de cada juagador en Hundir la Flota.

    Atributos:
      id_jugador (str): identificador del propietario del tablero.
      tamano (int): lado del tablero (usuario, máquina)
      tablero (np.ndarray): Barcos del jugador y disparos recibidos.
      disparos (np.ndarray): Solo los disparos recibidos, sin barcos.
    """
    def __init__(self, id_jugador, tamano = TAMANO, barcos = None):
        self.id_jugador = id_jugador
        self.tamano = tamano
        self.barcos = dict(BARCOS if barcos is None else barcos) #"BARCOS" viene del variables.py; se copia para no modificar el original
        self.tablero = np.full((tamano, tamano), vacio) #vacio nombre temporal viene de variables.py
        self.disparos = np.full((tamano, tamano,), vacio) 
        self.posiciones = {}