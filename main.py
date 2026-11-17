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

        tablero_jugador.mostrar()
        tablero_maquina.mostrar(ocultar_barcos = True)

        disparo_jugador = pedir_coordenadas()
        fila = disparo_jugador[0]
        columna = disparo_jugador[1]

        resultado_disparo = tablero_maquina.recibir_disparo(fila,columna)
        print(MENSAJES["impacto"],resultado_disparo)

        if resultado_disparo == MENSAJES["impacto"]: # Si el disparo acierta vuelves a disparar, a menos que ya no queden barcos y hayas ganado

            if tablero_maquina.quedan_barcos() == False:
                print(MENSAJES["victoria"])
                break

        elif resultado_disparo == MENSAJES["fallo"]: # Si el disparo ha fallado, el turno pasa a ser de la máquina
            turno = "maquina"

    else: # El turno de la máquina, funciona igual que el turno de jugador pero disparando a tu tablero
        print(MENSAJES["turno_maquina"])

        disparo_maquina = disparo_aleatorio()
        fila = disparo_maquina[0]
        columna = disparo_maquina[1]

        print(f"La máquina ha disparado a la casilla: {fila, columna}")

        resultado_disparo = tablero_jugador.recibir_disparo(fila,columna)
        print(MENSAJES["impacto"],resultado_disparo)

        if resultado_disparo == MENSAJES["impacto"]:

            if tablero_jugador.quedan_barcos() == False:
                print(MENSAJES["derrota"])
                break

        elif resultado_disparo == MENSAJES["fallo"]:
            turno = "jugador"
