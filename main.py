'''
main.py es el encargado de ejecutar el programa juntando el código de todo el proyecto
importando la clase Tablero, las funciones y variables del resto de archivos.
"python main.py" será el comando para poder empezar a jugar.
'''

from variables import MENSAJES
from funciones import mostrar_instrucciones, pedir_coordenadas, disparo_aleatorio
from clases import Tablero

print("=" * 60)
print(MENSAJES["bienvenido"])
print("=" * 60)

mostrar_instrucciones()

tablero_jugador = Tablero("jugador")
tablero_maquina = Tablero("maquina")

# Los barcos se colocan una sola vez antes de empezar, para ambos tableros.
tablero_jugador.colocar_todos_los_barcos()
tablero_maquina.colocar_todos_los_barcos()

turno = "jugador" # Definimos de quién es el turno antes del bucle, el jugador empieza siempre

while True: # Cada vuelta del bucle es un disparo

    if turno == "jugador":
        print(MENSAJES["turno_jugador"])
        disparo_jugador = pedir_coordenadas()
        fila = disparo_jugador[0]
        columna = disparo_jugador[1]

        turno = "maquina" # De momento el turno cambia siempre, falta que repita si acierta

    else:
        print(MENSAJES["turno_maquina"])
        disparo_maquina = disparo_aleatorio()
        fila = disparo_maquina[0]
        columna = disparo_maquina[1]
        print(f"La máquina ha disparado a la casilla: {fila, columna}")

        turno = "jugador"
