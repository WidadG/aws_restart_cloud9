"""
Ejercicio 1: Uso de os.system
"""
import os
import subprocess

#  recibe un argumento de tipo String, en este caso ocuparemos ls
os.system("ls")
#El resultado debería mostrar el contenido de su directorio actual.

"""
Ejercicio 2: Uso de subprocess.run
"""
subprocess.run(["ls"])

"""
Ejercicio 3: Uso de subprocess.run con dos argumentos
"""
subprocess.run(["ls","-l"])

"""
Ejercicio 4: Uso de subprocess.run con tres argumentos
"""
subprocess.run(["ls","-l","README.md"]) #El tercer argumento es el nombre del directorio

"""
Ejercicio 5: Recuperación de información del sistema
"""
command="uname" #comando del sistema operativo que proporciona información sobre el sistema
commandArgument="-a" #hace que muestre información detallada sobre el sistema.
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

"""
Ejercicio 6: Recuperación de información sobre el espacio en disco
"""
command="ps" #se utiliza en sistemas Unix y Linux para mostrar información sobre los procesos en ejecución.
commandArgument="-x" #le dice a ps que muestre todos los procesos, no solo aquellos que están asociados con una terminal.
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
#Utiliza la función run() del módulo subprocess para ejecutar el comando ps con el argumento -x. Los argumentos se pasan como una lista.