"""
Aca definimos el tamaño del tablero que usara el Deb1
"""
TAMANO_TABLERO = 10

"""
Cree un diccionario "BARCOS" la equivalenncia de 'Clave' seria el nombre de cada barco
el cual ocupa 'Valor' como su tamaño
"""
BARCOS = {
    "portaaviones_ivan" : 4,
    "acorazado_rafa" : 3,
    "acorazado_rocio" : 3,
    "destructor_oscar" : 2,
    "destructor_iluis" : 2,
    "destructo_samuel" : 2,
    "bote_challenge" : 1,
    "bote_thebridge" : 1,
    "bote_slack" : 1,
    "bote_kahoot" : 1
}

"""
Este diccionario "SIMBOLOS" con tiene 'Clave' el nombre que usaran los deb´s en sus funciones y clases
con el 'Valor' seria el emoji que ocuparia la visualizacion
"""
SIMBOLOS = {
    "agua" : "💧",
    "barco" : "⬜",
    "impacto" : "💥",
    "fallo" : "👎"
}

"""
El diccionario "MENSAJES" contiene la 'Clave:Valor' de los mensajes que usaran los deb´s para mostrar
en las respectivas funciones
"""
MENSAJES = {
    "bienvenido" : "Bienvenido jugador a Hundir La Flota!",
    "turno_jugador" : "Es tu turno",
    "turno_maquina" : "Es el turno de la maquina!",
    "impacto" : "BIEN! Le diste!!",
    "impacto_maquina" : "Auch, Capitán Iván te ha dado!!",
    "fallo" : "Fallaste, le diste al agua!",
    "fallo_maquina" : "La maquina falló, le dió al agua!",
    "impacto_maquina" : "Le maquian fue pilla y te dió",
    "fallo" : "Fallaste, le diste al agua!",
    "fallo_maquina" : "La maquina ha fallado, le dio al agua",
    "repetido" : "Ya has disparado a esta posicion, intenta de nuevo!",
    "invalido" : "Coordenadas incorrectas, te saliste del tablero.",
    "victoria" : "Muy bien, has ganado!",
    "derrota" : "Mal ahí, perdiste. Te ha derrotado el capitan Ivan Nosuspende!"
}


"""
Estas 2 listas/variables las cree para que se guardara los disparos realizados tanto por la maquina
como por el jugador
"""
casillas_disparadas_jugador = []
casillas_disparadas_maquina = []
