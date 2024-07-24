"""
Ejercicio 1: Creación del archivo de datos de moléculas JSON
Se creará un archivo jSON para que luego sea utilizado en este script.
"""
"""
Ejercicio 2: Creación del módulo controlador de archivos JSON
"""
import json

def leerJsonFile(fileName):
    datos = ""  # Inicializar la variable de datos como una cadena vacía
    try:
        with open(fileName) as json_file:  # Abrir el archivo JSON
            datos = json.load(json_file)  # Cargar el contenido JSON en un diccionario
    except IOError:
        print("No se pudo leer el archivo")  # Manejar el error si no se puede abrir el archivo
    return datos  # Devolver el contenido del archivo o una cadena vacía
