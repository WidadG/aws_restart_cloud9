"""
Ejercicio 1: Creación de una función definida por el usuario
"""
def getDoubleAlphabet(alphabet): #Definimos una nueva funcion
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

# Ejemplo de uso
#alphabet = "ABC"
#result = getDoubleAlphabet(alphabet)
#print(result)  # Esto imprimirá "ABCABC"

"""
Ejercicio 2: Cifrado de un mensaje
"""
def getMessage():  #define una función llamada getMessage que no toma ningún argumento.
    stringToEncrypt = input("Ingresa un mensaje para encriptar: ") #utiliza la función input() para solicitar al usuario que ingrese un mensaje. 
    #El mensaje ingresado se almacena en la variable stringToEncrypt.
    return stringToEncrypt
    
# Ejemplo de uso
#message = getMessage()
#print("El mensaje para encriptar es:", message)

"""
Ejercicio 2: Cifrado de un mensaje
"""
def getCipherKey(): #define una función llamada getCipherKey que no toma ningún argumento.
    shiftAmount = input("Ingresa una llave (con numeros del 1-25): ") #para solicitar al usuario que ingrese una clave de cifrado. 
    #El valor ingresado se almacena en la variable shiftAmount.
    return shiftAmount
    
# Ejemplo de uso
#key = getCipherKey()
#print("The cipher key is:", key)

"""
Ejercicio 4: Cifrado de un mensaje
"""
def encryptMessage(message, cipherKey, alphabet): # define la función que toma tres argumentos.
    encryptedMessage = ""
    uppercaseMessage = message.upper()  # Convertir el mensaje a mayúsculas

    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)  # Buscar la posición de la letra actual
        if position != -1:  # Verificar si la letra está en el alfabeto
            newPosition = (position + int(cipherKey)) % len(alphabet)  # Calcular la nueva posición
            encryptedMessage += alphabet[newPosition]  # Agregar la nueva letra al mensaje cifrado
        else:
            encryptedMessage += currentCharacter  # Agregar la letra actual si no está en el alfabeto

    return encryptedMessage  # Devolver el mensaje cifrado

# Ejemplo de uso
#alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#message = getMessage()  # Suponiendo que has definido esta función
#cipherKey = getCipherKey()  # Suponiendo que has definido esta función
#encrypted = encryptMessage(message, cipherKey, alphabet)
#print("Mensaje encriptado:", encrypted)

"""
Ejercicio 5: Descifrado de un mensaje
"""

def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)  # Calcular la clave de descifrado negando la clave de cifrado
    #Esto se logra multiplicando la clave de cifrado por -1
    return encryptMessage(message, decryptKey, alphabet)  # Llamar a encryptMessage con la clave de descifrado

# Ejemplo de uso
#alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#message = "ENCRYPTEDMESSAGE"
#cipherKey = "5"
#decrypted = decryptMessage(message, cipherKey, alphabet)
#print("Decrypted message:", decrypted)

"""
Ejercicio 6: Creación de una función principal
"""

def runCaesarCipherProgram():
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Definir el alfabeto
    print(f'Alphabet: {myAlphabet}')  # Imprimir el alfabeto
    myAlphabet2 = getDoubleAlphabet(myAlphabet)  # Duplicar el alfabeto
    print(f'Alphabet2: {myAlphabet2}')  # Imprimir el alfabeto duplicado
    myMessage = getMessage()  # Obtener el mensaje del usuario
    print(myMessage)  # Imprimir el mensaje ingresado
    myCipherKey = getCipherKey()  # Obtener la clave de cifrado
    print(myCipherKey)  # Imprimir la clave ingresada
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)  # Cifrar el mensaje
    print(f'Encrypted Message: {myEncryptedMessage}')  # Imprimir el mensaje cifrado
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)  # Descifrar el mensaje
    print(f'Decrypted Message: {myDecryptedMessage}')  # Imprimir el mensaje descifrado

# Llamar a la función para ejecutar el programa
runCaesarCipherProgram()