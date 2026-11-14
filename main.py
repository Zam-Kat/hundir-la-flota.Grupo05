'''
main.py es el encargado de ejecutar el programa juntando el código de todo el proyecto
importando la clase Tablero, las funciones y variables del resto de archivos.
"python main.py" será el comando para poder empezar a jugar.
'''

from variables import MENSAJES
from funciones import mostrar_instrucciones

print("=" * 60)
print(MENSAJES["bienvenido"])
print("=" * 60)

mostrar_instrucciones()
