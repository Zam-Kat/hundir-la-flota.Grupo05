'''
Qué se incluye aquí (instrucciones):
Todas las funciones que no son metodos de `Tablero`:
- Pedir y validar las coordenadas del jugador
- Elegir el disparo de la maquina sin repetir casilla
- Imprimir las instrucciones, ...
'''
import numpy as np
import random
from variables import MENSAJES, TAMANO_TABLERO
#print(MENSAJES["nombre_mensaje"])


#casillas_disparadas_jugador=list() Esta lista tiene que venir de variables.py

#pedir_coordenadas -Función que pide al jugador las coordenadas donde dispara: int, rango, que no haya vacíos
#Uso IA: aquí he pedido ayuda a la IA para el "except ValueError as" porque no conseguía que me saltaran los errores concretos.
#mejoras pendientes:
#- quiero que si te equivocas en la columna, no vuelva a empezar en fila, sino que te pida la columna
def pedir_coordenadas():
    while True:
        try:
            fila = int(input("Coordenadas fila:"))
            columna = int(input("Coordenadas columna:")) #Unificar input fila y columna
            if fila < 0 or fila > TAMANO_TABLERO or columna < 0 or columna > TAMANO_TABLERO 
                raise ValueError(MENSAJES["invalido"]) #error_concreto de fuera de rango

            if (fila,columna) in casillas_disparadas_jugador:
                raise ValueError(MENSAJES["repetido"]) #error_concreto de casilla repetida
            
            casillas_disparadas_jugador.append((fila, columna))
            return (fila, columna)
            
        except ValueError as error_concreto:
            print(error_concreto)
            print("El disparo tiene que ser un número, caer dentro del tablero y no vale repetir") #Duda: ¿queremos que saque esto siempre?


#disparo_maquina -Función que hace el disparo de la máquina: aleatorio y nunca repite casilla
casillas_disparadas_maquina=list() #Creamos una lista donde vamos a acumular las casillas donde dispara la máquina
def disparo_aleatorio():
    while True:
            fila = np.random.randint(fila_min, fila_max)
            columna = np.random.randint(columna_min, columna_max)
        
            if (fila,columna) not in casillas_disparadas_maquina:            
                casillas_disparadas_maquina.append((fila, columna))
            return (fila, columna)



#mostrar_puntuacion -Función que muestra el score de puntuaciones: máquina vs jugador
#Aquí depende de como Lluis configure el nombre de la variable de aciertos
aciertos_jugador = 3
aciertos_maquina = 2
def mostrar_puntuacion():
    print("     MARCADOR\n")
    print(f"- Jugador: {aciertos_jugador} puntos")
    print(f"- Máquina: {aciertos_maquina} puntos")
    print(f"Total disparos: {len(casillas_disparadas_jugador)}")

#mostrar_instrucciones -Función que imprime las instrucciones
'''
uso IA: le dije este promt a gemini:
Tengo que hacer el def mostrar_instrucciones de este juego (y le puse el pantallazo del "como funciona")
Estas son las reglas del juego. Quiero hacer un print de un texto con puntos por pasos(1, 2, 3, 4)
que sea breve, original y divertido, estilo "bienvenida al juego donde tienes que derrotar el barco enemigo o algo así"
¿Me puedes dar el texto para los distintos prints?
'''
def mostrar_instrucciones():
        print("=" * 60)
        print(" ⚓ ¡BIENVENIDO AL COMBATE NAVAL, COMANDANTE! ⚓ ")
        print("=" * 60)
        print(
        "Estás a punto de enfrentarte en una versión táctica y directa"
        " contra la máquina."
        )
        print("Tu misión: cazar y hundir toda su flota antes de que ella hunda" " la tuya.\n")

        print("--- REGLAS DE COMBATE ---")
        print(
        "1. Duelo a muerte: Jugador (tú) contra la máquina. Cada uno tiene un"
        " tablero de 10x10 casillas."
        )
        print(
        "2. Flota oculta: Al empezar se despliegan 10 barcos al azar por tablero:\n"
        "   • 4 barcos de 1 casilla\n"
        "   • 3 barcos de 2 casillas\n"
        "   • 2 barcos de 3 casillas\n"
        "   • 1 barco de 4 casillas\n"
        "   (En total, 20 casillas enemigas que mandar a fondo del mar)."
        )
        print(
        "3. ¡Abrid fuego!: Se juega por turnos y... ¡empiezas tú! Introduce"
        " coordenadas de ataque (fila y columna del 0 al 9)."
        )
        print(
        "4. Dinámica de aciertos: Si aciertas en un barco enemigo, ¡repites"
        " turno! Si das en agua, el turno pasa a la máquina (que disparará a"
        " una casilla aleatoria de tu tablero)."
        )
        print(
        "5. Victoria: Gana el primer almirante que consiga hundir los 20"
        " cascos de los barcos rivales."
        )
        print("\n[ Sistemas de seguridad activados: Si disparas a una casilla")
        print("repetida o escribes coordenadas inválidas, el radar te avisará")
        print("sin penalizarte. ¡Ningún error tonto romperá el juego! ]")
        print("=" * 60)
    else:
        print("Ok, si no tienes dudas, ¡seguimos con el juego!")

#Para poder hacer pruebas, temporalmente voy a poner que se repitan los disparos un número de 3 turnos
for turno in range(3):
    print (f"--------TURNO: {turno+1}--------\n")
    disparo_jugador = pedir_coordenadas()
    disparo_maquina =disparo_aleatorio()
    print (f"\nEn el turno {turno+1} tú has disparado a la casilla{disparo_jugador}\nLa máquina te ha disparado a {disparo_maquina}")
    print(f"Historial de disparos:\n- Jugador: {casillas_disparadas_jugador}\n- Máquina: {casillas_disparadas_maquina}\n\n")
print("FIN DE LA RONDA:\n")
print(mostrar_puntuacion())
print(mostrar_instrucciones())
