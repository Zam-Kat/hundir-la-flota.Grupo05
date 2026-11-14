'''
Todas las funciones que no son metodos de `Tablero`:
- Pedir y validar las coordenadas del jugador
- Elegir el disparo de la maquina sin repetir casilla
- Imprimir las instrucciones, ...
'''
import numpy as np
import random

# CONFIG 
# Tamaño tablero: pendiente ver cómo lo define Samuel
# Definimos valores mínimos y máximos del tablero, por si cambian sus dimensiones en el futuro
fila_min = 0
fila_max = 9
columna_min = 0
columna_max = 9


casillas_disparadas_jugador=list() #Creamos una lista donde vamos a acumular las casillas donde disparamos

#pedir_coordenadas -Función que pide al jugador las coordenadas donde dispara: int, rango, que no haya vacíos
#Uso IA: aquí he pedido ayuda a la IA para el "except ValueError as" porque no conseguía que me saltaran los errores personalizados.
#mejoras pendientes:
#- quiero que si te equivocas en la columna, no vuelva a empezar en fila, sino que te pida la columna
def pedir_coordenadas():
    while True:
        try:
            fila = int(input("Introduce la fila del disparo: "))
            if fila < fila_min or fila > fila_max:
                raise ValueError(f"\nCuidado, ¡te has salido del tablero! La fila debe estar entre {fila_min} y {fila_max}") #error_concreto de fuera de rango
            
            columna = int(input("Introduce la columna del disparo: "))
            if columna < columna_min or columna > columna_max:
                raise ValueError(f"\nCuidado, ¡te has salido del tablero! La columna debe estar entre {columna_min} y {columna_max}") #error_concreto de fuera de rango

            if (fila,columna) in casillas_disparadas_jugador:
                raise ValueError(f"\nYa has disparado a la casilla ({fila},{columna}), prueba otra") #error_concreto de casilla repetida
            
            casillas_disparadas_jugador.append((fila, columna))
            return (fila, columna)
            
        except ValueError as error_concreto:
            print(error_concreto)
            print("El disparo tiene que ser un número, caer dentro del tablero y no vale repetir")


#Para poder hacer pruebas, temporalmente voy a poner que se repitan los disparos un número de 3 turnos

for turno in range(3):
    print (f"--------TURNO: {turno+1}--------\n")
    disparo_jugador = pedir_coordenadas()
    print (f"\nEn el turno {turno+1} has disparado a la casilla{disparo_jugador}")
    print(f"Historial de disparos: {casillas_disparadas_jugador}\n\n")


#disparo_maquina -Función que hace el disparo de la máquina: aleatorio y nunca repite casilla



#mostrar_puntuacion -Función que muestra el score de puntuaciones: máquina vs jugador

#mostrar_instrucciones -Función que imprime las instrucciones
