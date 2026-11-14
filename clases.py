import random
import numpy as np



class Tablero:
    """
    Tablero de cada juagador en Hundir la Flota.

    Atributos:
      id_jugador (str): identificador del propietario del tablero.
      tamano (int): lado del tablero (usuario, máquina)
      tablero (np.ndarray): Barcos del jugador y disparos recibidos.
      disparos (np.ndarray): Solo los disparos recibidos, sin barcos.
    """
    def __init__(self, id_jugador, tamano = TAMANO_TABLERO, barcos = None):
        self.id_jugador = id_jugador
        self.tamano = tamano
        self.barcos = dict(BARCOS if barcos is None else barcos) #"BARCOS" viene de variables.py; se copia para no modificar el original
        self.tablero = np.full((tamano, tamano), SIMBOLOS["agua"]) #SIMBOLO viene de variables.py
        self.disparos = np.full((tamano, tamano,), SIMBOLOS["agua"])
        self.posiciones = {}

    def cabe_barco(self, casillas):
        """
        Comprueba si un barco se puede colocar en las casillas de TAMANO_TABLERO antes de su colocación
        
        Un barco se puede colocar si:
          1. Todas sus casillas están dentro del tablero
          2. No hay ningún barco en esas casillas ni en las 8 casillas que le rodean
          (así siempre queda una casilla de agua entre barcos)

          Argumentos:
            casillas: lista de tuplas [int, int]. Primero se comprueba que la casilla donde queremos incorporar el barco existe.
            Luego que en una zona 3x3 no existe ningún otro elemento "barco". 

            Returns:
              bool: True si se puede colocar, False para el caso contrario.
        """

        for fila, columna in casillas:
            if not (0 <= fila < self.tamano and 0 <= columna < self.tamano):
                return False
            fila0, fila1 = max(fila -1, 0), min(fila + 2, self.tamano)
            columna0, columna1 = max(columna -1, 0), min(columna + 2, self.tamano)
            if (self.tablero[fila0:fila1, columna0, columna1] == SIMBOLOS["barco"]).any():
                return False
        return True