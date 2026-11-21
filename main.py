'''
main.py es el encargado de ejecutar el programa juntando el código de todo el proyecto
importando la clase Tablero, las funciones y variables del resto de archivos.
"python main.py" será el comando para poder empezar a jugar.
'''

from variables import MENSAJES
from funciones import mostrar_instrucciones, pedir_coordenadas, disparo_aleatorio
from clases import Tablero

print("=" * 60)
print(MENSAJES["bienvenido"].center(60))
print("=" * 60)

# Menú de inicio con un bucle
while True:
    print("\n1. Jugar")
    print("2. Ver instrucciones")
    print("3. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        break
    elif opcion == "2":
        mostrar_instrucciones()
    elif opcion == "3":
        exit()
    else:
        print("Esa opción no existe, prueba otra vez.")

tablero_jugador = Tablero("jugador")
tablero_maquina = Tablero("maquina")

# Los barcos se colocan una sola vez antes de empezar, para ambos tableros.
tablero_jugador.colocar_todos_los_barcos()
tablero_maquina.colocar_todos_los_barcos()

turno = "jugador" # Definimos de quién es el turno antes del bucle, el jugador empieza siempre

while True: # Cada vuelta del bucle es un disparo

    if turno == "jugador":

        print("\n" + "=" * 60)
        print(MENSAJES["turno_jugador"].center(60))
        print("=" * 60)


        barcos_maquina = len(tablero_maquina.barcos_restantes()) # Contador de barcos que le quedan a la máquina
        print(f"A la máquina le quedan {barcos_maquina} barcos")

        tablero_jugador.mostrar()
        tablero_maquina.mostrar(ocultar_barcos = True)

        disparo_jugador = pedir_coordenadas()

        resultado_jugador = tablero_maquina.recibir_disparo(disparo_jugador)
        print(resultado_jugador)

        hundidos_antes = len(tablero_maquina.barcos_hundidos()) # Cuenta barcos hundidos antes del disparo


        if resultado_jugador == MENSAJES["impacto"]: # Si el disparo acierta vuelves a disparar, a menos que ya no queden barcos y hayas ganado

            if len(tablero_maquina.barcos_hundidos()) > hundidos_antes: # Si el contador de barcos hundidos ha subido después del disparo, mensaje de tocado y hundido
                print("Tocado y hundido!")

            if tablero_maquina.quedan_barcos() == False:
                print("\n" + "=" * 60)
                print(MENSAJES["victoria"].center(60))
                print("=" * 60)

                tablero_jugador.mostrar() # Mostramos los dos tableros al final de cada partida, lo mismo cuando pierdes
                tablero_maquina.mostrar()
                break

        elif resultado_jugador == MENSAJES["fallo"]: # Si el disparo ha fallado, el turno pasa a ser de la máquina
            turno = "maquina"

    else: # El turno de la máquina, funciona igual que el turno de jugador pero disparando a tu tablero
        print("\n" + "=" * 60)
        print(MENSAJES["turno_maquina"].center(60))
        print("=" * 60)


        disparo_maquina = disparo_aleatorio()

        print(f"La máquina ha disparado a la casilla: {disparo_maquina}")

        hundidos_antes = len(tablero_maquina.barcos_hundidos())


        resultado_maquina = tablero_jugador.recibir_disparo(disparo_maquina)
        print(resultado_maquina)

        if resultado_maquina == MENSAJES["impacto"]:
            if len(tablero_maquina.barcos_hundidos()) > hundidos_antes:
                print("Tocado y hundido!")

            if tablero_jugador.quedan_barcos() == False:
                print("\n" + "=" * 60)
                print(MENSAJES["derrota"].center(60))
                print("=" * 60)

                tablero_jugador.mostrar()
                tablero_maquina.mostrar()
                break


        elif resultado_maquina == MENSAJES["fallo"]:
            input("\nPulsa Enter para continuar...") # Pausa para cambio de turno
            turno = "jugador"
