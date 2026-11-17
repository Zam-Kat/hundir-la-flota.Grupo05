import random
import numpy as np
import string
from variables import TAMANO_TABLERO, SIMBOLOS, BARCOS, MENSAJES  



class Tablero:
    """
    Tablero de cada juagador en Hundir la Flota.

    Atributos:
      id_jugador (str): identificador del propietario del tablero.
      tamano (int): lado del tablero (usuario, máquina)
      tablero (np.ndarray): Barcos del jugador y disparos recibidos.
      disparos (np.ndarray): Solo los disparos recibidos, sin barcos.
      posiciones (dict[str, lista[tuplas[int, int]]]). Se rellena en colocar_barcos() y sirve para saber qué barcos están hundidos.
    """

    def __init__(self, id_jugador, tamano = TAMANO_TABLERO):
        self.id_jugador = id_jugador
        self.tamano = tamano
        self.barcos = BARCOS #"BARCOS" viene de variables.py; se copia para no modificar el original
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
            # Comprobación dentro de tablero
            if not (0 <= fila < self.tamano and 0 <= columna < self.tamano):
                return False
            # Comprobación zona 3x3 alrededor de la casilla
            fila0, fila1 = max(fila -1, 0), min(fila + 2, self.tamano)
            columna0, columna1 = max(columna -1, 0), min(columna + 2, self.tamano)
            if (self.tablero[fila0:fila1, columna0, columna1] == SIMBOLOS["barco"]).any():
                return False
        return True

    def colocar_un_barco(self, barco, eslora, max_intentos=100):
        """
        Intenta colocar un barco en una posición aleatoria dentro del tablero.
        
        Prueba hasta max_intentos veces con una casilla de inicio y una orientación horizontal o vertial al azar.
        
        Argumentos:
            barco (str): nombre del barco.
            eslora(int): número de casillas que ocupa el barco a colocar.
            max_intentos (int): intentos máximos antes de rendirse.
        
        Returns:
            bool: True si el barco se ha colocado, False si no ha encontrado sitio.
        """
        for intentos in range(max_intentos):
            fila_inicial = random.randrange(self.tamano)
            columna_inicial = random.randrange(self.tamano)
            d_fila, d_columna = random.choice([(0,1), (1,0)]) # elige la orientación del barco al azar
            casillas = [(fila_inicial + i * d_fila, columna_inicial + i * d_columna) for i in range(eslora)]
            if self.cabe_barco(casillas):
                for fila, columna in casillas:
                    self.tablero[fila, columna] = SIMBOLOS["barco"]
                    self.posiciones[barco] = casillas
                    return True
        return False

    def colocar_todos_los_barcos(self, max_reinicios = 999):
        """
        Coloca todos los barcos en posiciones aleatorias
        
        Para cada eslora del diccionario BARCOS se colocan tantos barcos como haya- Cada barcoqueda entero dentro
        del tablero y separado de los demás por al menos una casilla de agua tal como se ha definido en la función
        cabe_barco. Se colocan de mayor a menor eslora, porque así es más fácil que quepan todos. Si algún barco
        no encuentra sitio, se vacía el tablero y se vuelve a empezar, hasta un maximo de reinicios.
        
        Argumentos:
            max_reinicios(int): número máximo de veces que se vacia el tablero y se empieza de nuevo. Por defecto 999
            
        Returns:
            None: modifica tablero y posiciones en el propio objeto.
            
        Raises:
            RuntimeError: si tras completar los reinicios determinados por max_reinicios no se han podido colocar
            todos los barcos se lanza este error.
        """
        lista = [
            (f"barco{eslora}-{n}", eslora)
            for eslora, cantidad in sorted(self.barcos.items(), reverse=True)
            for n in range(1, cantidad + 1)
        ]
        for intentos in range(max_reinicios):
            self.tablero[:] = SIMBOLOS["agua"]
            self.disparos[:] = SIMBOLOS["agua"]
            self.posiciones = {}
            if all(self.colocar_un_barco(n,e) for n, e in lista):
                return
        raise RuntimeError(f"No se han podido colocar todos los barcos tras {max_reinicios} intentos")

    # ------------------Disparos----------------------------
    def recibir_disparo(self, fila_columna):
        """
        Procesa un disparo recibido en una casilla
        
        Marca el resultado en los dos tableross con SIMBOLOS ["impacto"] si había barco o SIMBOLOS["fallo"]
        si había agua.

        Argumentos:
            fila_columna (tupla[int, int]): casilla disparada como (fila, columna), con valores de 0 a -1.

        Returns:
            str: "tocado" si había barco, "agua" si no, o "repetido" si ya se había disparado antes a esa casilla.

        Raises: 
            ValueError: si la casilla está fuera del tablero (el juego puede mostrar entonces MENSAJES["invalido"],
            de variables.py)
        """
        fila, columna = fila_columna
        if not (0 <= fila < self.tamano and 0 <= columna < self.tamano):
            raise ValueError(MENSAJES["invalido"]) # DUDAS de si ponerlo dado que Rocio define función disparo aleatorio
        if self.disparos[fila, columna] != SIMBOLOS["agua"]:
            return "repetido"
        if self.tablero[fila, columna] == SIMBOLOS["barco"]:
            self.tablero[fila, columna] = SIMBOLOS["impacto"]
            self.disparos[fila, columna] = SIMBOLOS["impacto"]
            return MENSAJES["impacto"]
        self.tablero[fila, columna] = SIMBOLOS["fallo"]
        self.disparos[fila, columna] = SIMBOLOS["fallo"]
        return MENSAJES["fallo"]

    # ------------------Consultas (opcional)---------------------
    def quedan_barcos(self):
        """
        Indica si al jugador le queda algún barco sin tocar.
        
        Sirve para detectar el final de la partida: cuando devuelve False, el jugador ha perdido.
        
        Returns:
            bool: True si aún hay casillas de barco sin tocar, False si no.
        """
        return bool((self.tablero == SIMBOLOS["barco"]).any())

    def barco_hundido(self, barco):
        """
        Indica si un barco concreto está hundido.
        
        Argumentos:
            barco (str): nombre del barco (clave de posiciones).
        
        Returns: 
            bool: True si todas las casiilas del barco están tocadas.
        """

        return all(self.tablero[fila, columna] == SIMBOLOS["impacto"]
                   for fila, columna in self.posiciones[barco])

    def barcos_restantes(self):
        """
        Devuelve los nombres de los barcos que aún no están hundidos.
        
        Returns:
            lista[str]: nombres de los barcos sin hundir.
        """
        return [barco for barco in self.posiciones if not self.barco_hundido(barco)]

    def barcos_hundidos(self):
        """
        Devuelve los nombres de los barcos que se han hundido.
        
        Returns:
            lista[str]: nombres de los barcos hundidos.
        """
        return[barco for barco in self.posiciones if self.barco_hundido(barco)]
    
    # ------------------Visualizacion----------------------------
    def mostrar(self, ocultar_barcos=False):
        """
        Imprime el tablero por pantalla, con índices de fila y columna.
        
        Argumentos:
            ocultar_barcos (bool): si es True se imprime self.disparos (sin barcos). Si es False (por defecto)
            se imprime self.tablero.
        
        Returns:
            None: solo imprime por pantalla.
        """
        if ocultar_barcos:
            matriz = self.disparos 
        else:
            self.tablero
        print(f"Tablero de {self.id_jugador}")
        # Cabecera con letras (A, B, C... para las columnas. Help IA)
        print("   " + " ".join(string.ascii_uppercase[: self.tamano]))
        print("  +" + "-" * (2 * self.tamano - 1) + "+")
        # Marco para los laterales para ayudar con la visualización (help IA)
        for i, fila in enumerate(matriz):
            print(f"{i:>2}  |" + " ".join(fila) + "|")
        print("  +" + "-" * (2 *self.tamano - 1) + "+")

    