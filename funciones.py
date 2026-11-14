'''
Todas las funciones que no son metodos de `Tablero`:
- Pedir y validar las coordenadas del jugador
- Elegir el disparo de la maquina sin repetir casilla
- Imprimir las instrucciones, ...
'''
import numpy as np
import random

# CONFIG 
# Tamaño tablero
# Definimos valores mínimos y máximos del tablero, por si cambian sus dimensiones en el futuro
fila_min = 0
fila_max = 9
columna_min = 0
columna_max = 9

#pedir_coordenadas -Función que pide al jugador las coordenadas donde dispara: int, rango, que no haya vacíos
#Uso IA: aquí he pedido ayuda a la IA para el "except ValueError as" porque no conseguía que me saltaran los errores personalizados.
#mejoras pendientes: quiero que si te equivocas en la columna, no vuelva a empezar en fila, sino que te pida la columna
def pedir_coordenadas():
    while True:
        try:
            fila = int(input("Introduce la fila del disparo: "))
            if fila < fila_min or fila > fila_max:
                raise ValueError(f"Cuidado, ¡te has salido del tablero! La fila debe estar entre {fila_min} y {fila_max}") #Error de fuera_rango
            
            columna = int(input("Introduce la columna del disparo: "))
            if columna < columna_min or columna > columna_max:
                raise ValueError(f"Cuidado, ¡te has salido del tablero! La columna debe estar entre {columna_min} y {columna_max}") #Error de fuera_rango

            return (fila, columna)
        
        except ValueError as fuera_rango:
            print(fuera_rango)
            print("Por favor, introduce coordenadas válidas")

disparo_jugador = pedir_coordenadas()
print ("Has disparado a la casilla",{disparo_jugador})

#disparo_maquina -Función que hace el disparo de la máquina: aleatorio y nunca repite casilla


#mostrar_puntuacion -Función que muestra el score de puntuaciones: máquina vs jugador

#mostrar_instrucciones -Función que imprime las instrucciones
