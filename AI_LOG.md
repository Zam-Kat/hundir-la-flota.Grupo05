# AI_LOG · Team Challenge Hundir la flota

Este registro no cuenta para la nota. Sirve para ver dónde vais solos y dónde os apoyáis. Si no habéis usado IA en una parte, dejad el nivel en 0: también es un dato útil.

**Grupo:** Lluis Hernandez, Rocío Moya, Óscar Hernández, Samuel Zuccato

**Herramientas usadas:** Cloude, Gemini, ChatGPT

> El repositorio es público: no pongáis datos personales ni contraseñas en los prompts que copiéis aquí.

## Resumen por módulo

Niveles: **0** sin IA · **1** consulta puntual, el código es nuestro · **2** la IA escribe partes y las adaptamos · **3** casi todo lo escribe la IA

| Módulo | Quién lo ha llevado | Nivel de IA (0-3) | Nº de prompts | ¿Lo podríais repetir sin IA? (sí / en parte / no) |
|---|---|---|---|---|
| `variables.py` | Samuel Z| 1 | 1 | sí |
| `clases.py` | Lluis Hernanez | 2 | 3 | En parte |
| `funciones.py` | Rocío Moya | 1 | 2 | sí |
| `main.py` | Óscar Hernández | 1 | 3 | sí |
| `README.md` | Samuel Zuccato | 0 | 0 | 0 |

## Registro de prompts

Copiad este bloque por cada prompt que haya influido en vuestro código.

### Módulo Funciones.py / Rocío Moya · Prompt 1

- **Objetivo:** conseguir texto instrucciones
- **Prompt:** (le pasé captura de las reglas del juego del enunciado)Tengo que hacer el def mostrar_instrucciones de este juego (y le puse el pantallazo del “como funciona”). Estas son las reglas del juego. Quiero hacer un print de un texto con puntos por pasos(1, 2, 3, 4) que sea breve, original y divertido, estilo “bienvenida al juego donde tienes que derrotar el barco enemigo o algo así. ¿Me puedes dar el texto para los distintos prints?
- **Respuesta relevante:** copié todo el texto
- **Cambios:** sólo añadí los print() al principio de las frases
- **Comprobación:** probé la función mostrar_instrucciones()
- **Decisión propia:** Tengo que hacer el def mostrar_instrucciones de este juego (y le puse el pantallazo del “como funciona”). Estas son las reglas del juego. Quiero hacer un print de un texto con puntos por pasos(1, 2, 3, 4) que sea breve, original y divertido, estilo “bienvenida al juego donde tienes que derrotar el barco enemigo o algo así. ¿Me puedes dar el texto para los distintos prints?

### MóduloFunciones.py / Rocío Moya · Prompt 2

- **Objetivo:** conseguir que funcionaran todos los raise Value Error de “salir del tablero” o “disparo repetido”
- **Prompt:** Le pasé un pantallazo de la función pedir_coordenadas tal como la tenía, y le dije “por que no me lanza el value error de que me salí del tablero”
- **Respuesta relevante:**Al poner únicamente except ValueError:, estás atrapando el error, pero le estás diciendo a Python que imprima un texto fijo y genérico, ignorando por completo el mensaje personalizado largo que escribiste dentro del raise.¿Cómo solucionarlo? Para que imprima exactamente el aviso que pusiste en el raise, tienes que capturar el error en una variable (por ejemplo, llamándola e) usando as e, y luego imprimir esa variable:
- **Cambios:** en lugar de llamarlo “e” lo llamé “error_concreto”
- **Comprobación:** probé la función pedir_coordenadas con un mini bucle para repetir disparo
- **Decisión propia:** simplemente llamarlo de otra forma, error_concreto, y ponerme comentarios para tenerlos ubicados

### Módulo Clases.py / Lluís Hernández · Prompt 1

- **Objetivo:** Ver si poner un input para el nombre de usuario dentro de la clase tablero
- **Prompt:** Si quisieras que el usuario pusiera su nombre con input tendría que ir dentro de la clase Tablero?
- **Respuesta relevante:** la parte que usasteis, resumida. ¿El input() del nombre debe ir dentro de Tablero? No, es mejor que quede fuera. Hay tres razones: Una sola responsabilidad: Tablero guarda el estado y las reglas del tablero. Si también pide datos por teclado, queda mezclada la lógica del juego con la interfaz. La máquina también tiene tablero: esa instancia no debería pedir nada por teclado. Tendríais que meter condiciones como "si soy la máquina, no preguntes". Pruebas: un método que llama a input() es incómodo de probar o reutilizar, porque se queda esperando a que alguien escriba.
- **Cambios:** qué modificasteis y por qué. No modifiqué nada al no recomendarlo
- **Comprobación:** cómo verificasteis que funcionaba. No aplica
- **Decisión propia:** qué decidisteis vosotros. No incorporar

### Módulo Clases.py / Lluís Hernández · Prompt 2

- **Objetivo:** Incorporar letras en la cabecera de la matriz en def mostrar
- **Prompt:** en la cabecera de la matriz que he dibujado se podrían poner letras A. B, C... en vez de los números 0,1,2...? Te paso el código desarrollado por mi: def mostrar(self, ocultar_barcos=False): """ Imprime el tablero por pantalla, con índices de fila y columna.![alt text](image.png)
- **Respuesta relevante:**  la parte que usasteis, resumida. Sí, se puede, y es solo un cambio de presentación. Basta con sustituir la línea de la cabecera de mostrar(): ![alt text](image-1.png)
- **Cambios:** Implementé el código para la visualización de las letras
- **Comprobación:** Imprimir el tablero para visualizarlo
- **Decisión propia:** Incorporarlo provisionalmente hasta ver si Rocío pedía las cordenadas en número o mezcla de números y letras

### Módulo Clases.py / Lluís Hernández · Prompt 3

- **Objetivo:** Ajustar columnas emojis cabeceras
- **Prompt:** por qué no me casan las cabeceras A,B,C... con los emojis de SIMBOLOS? Te adjunto documentos variables.py y clases.py para validad.
- **Respuesta relevante:**  Los emojis ocupan dos columnas en pantalla, así que las letras de la cabecera no quedaban sobre sus casillas. He añadido un cálculo del ancho con unicodedata, y la cabecera separa las letras con ese ancho: ![alt text](image-3.png)
- **Cambios:** Implementé el código para la visualización de las letras ajustada a los emojis
- **Comprobación:** Imprimir el tablero para visualizarlo
- **Decisión propia:** Incorporarlo provisionalmente hasta ver si Rocío pedía las cordenadas en número o mezcla de números y letras

### Módulo variables.py / Samuel Zuccato · Prompt 1

- **Objetivo:** Explicarme mi labor como Scrum Master
- **Prompt:** Segun el archivo de instrucciones que te pase sobre el Team Challenge, cual es mi labor como Scrum Master, cuales son mis tareas?
- **Respuesta relevante:** Coordinar al equipo: organizar tareas, supervisar avances y ayudar a resolver bloqueos, Gestionar GitHub: controlar Issues, ramas, commits y Pull Requests, asegurando que se revisen y se integren correctamente, Documentación: responsabilizarme de variables.py, README.md, requirements.txt y AI_LOG.md, Supervisar la entrega: comprobar que todo funcione, esté integrado y documentado, y coordinar la presentación final.
- **Cambios:** 
- **Comprobación:** 
- **Decisión propia:** 


### Módulo main.py / Óscar Hernández · Prompt 1

- **Objetivo:** empezar el bucle de turnos con lo que ya estaba subido, clase Tablero aún no estaba subida
- **Prompt:**  "dame un bloque de pistas sin resolver código para empezar con el bucle de turnos sin la clase Tablero"
- **Respuesta relevante:** pistas para la variable turno el if/else de cada turno
- **Cambios:**  lo escribí yo con las pistas y corregí algunos fallos, no se guardaba el disparo y la máquina usaba pedir_coordenadas que es para el jugador
- **Comprobación:**  revisando el código antes del commit
- **Decisión propia:** usar [0] y [1] para sacar fila y columna, más tarde se borró porque ya no era necesario

### Módulo main.py / Óscar Hernández · Prompt 2

- **Objetivo:** crear los tableros y colocar los barcos
- **Prompt:** "dame pistas para la siguiente función de main, crear tableros y colocar los barcos a partir de la clase Tablero"
- **Respuesta relevante:** pistas para saber dónde mostrar los tableros y llamar a colocar_todos_los_barcos
- **Cambios:** lo puse antes del bucle para que se haga una sola vez
- **Comprobación:** mirando que los nombres coincidían con los de la clase Tablero
- **Decisión propia:** no usar nada que no estuviera ya subido por mis compañeros

### Módulo GitHub / Óscar Hernández · Prompt 3

- **Objetivo:** saber cuándo y cómo ejecutar la PR, merge y limpieza de mi rama
- **Prompt:** "cómo dev 3 desarrollador de main, cúando me toca hacer la PR y el merge a main"
- **Respuesta relevante:** la PR de main se abre y revisa cuándo el código ya ha sido probado por completo con el resto de ramas mergeadas
- **Cambios:** no se ha tocado el código
- **Comprobación:** ejecutando y probando una partida final para ver que todo funciona y poder abrir la PR
- **Decisión propia:** al principio cree la PR y la pasé a borrador hasta tener todo el código de los demás y poder probar una partida completa sin fallos.