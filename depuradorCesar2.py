"""
Ejercicio 2: Trabajo con el programa de cifrado César con errores - Parte 2
"""
# Módulo Laboratorio: Programa de Cifrado César Error #2
#
# En un laboratorio anterior, creaste un programa de cifrado César. Esta versión del
# programa tiene errores. Usa un depurador para encontrar el error y corregirlo.

# Duplicar el alfabeto dado
def obtenerAlfabetoDuplicado(alfabeto):
    alfabetoDuplicado = alfabeto + alfabeto
    return alfabetoDuplicado

# Obtener un mensaje para cifrar
def obtenerMensaje():
    cadenaACifrar = input("Por favor, introduce un mensaje para cifrar: ")
    return cadenaACifrar

# Obtener una clave de cifrado
def obtenerClaveCifrado():
    cantidadDesplazamiento = input("Por favor, introduce una clave (número entero del 1 al 25): ")
    return cantidadDesplazamiento

# Cifrar el mensaje
def cifrarMensaje(mensaje, claveCifrado, alfabeto):
    mensajeCifrado = ""
    mensajeMayusculas = ""
    mensajeMayusculas = mensaje.upper()  # Correccion del error: Convertir el mensaje a mayúsculas que antes no las convertía y por ende no se sabia la posicion.
    for caracterActual in mensajeMayusculas:
        posicion = alfabeto.find(caracterActual)
        nuevaPosicion = posicion + int(claveCifrado)
        if caracterActual in alfabeto:
            mensajeCifrado = mensajeCifrado + alfabeto[nuevaPosicion]
        else:
            mensajeCifrado = mensajeCifrado + caracterActual
    return mensajeCifrado

# Descifrar el mensaje
def descifrarMensaje(mensaje, claveCifrado, alfabeto):
    claveDescifrado = -1 * int(claveCifrado)
    return cifrarMensaje(mensaje, claveDescifrado, alfabeto)

# Lógica principal del programa
def ejecutarProgramaCifradoCesar():
    miAlfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alfabeto: {miAlfabeto}')
    miAlfabeto2 = obtenerAlfabetoDuplicado(miAlfabeto)
    print(f'Alfabeto2: {miAlfabeto2}')
    miMensaje = obtenerMensaje()
    print(miMensaje)
    miClaveCifrado = obtenerClaveCifrado()
    print(miClaveCifrado)
    miMensajeCifrado = cifrarMensaje(miMensaje, miClaveCifrado, miAlfabeto2)
    print(f'Mensaje Cifrado: {miMensajeCifrado}')
    miMensajeDescifrado = descifrarMensaje(miMensajeCifrado, miClaveCifrado, miAlfabeto2)
    print(f'Mensaje Descifrado: {miMensajeDescifrado}')

# Lógica principal
ejecutarProgramaCifradoCesar()