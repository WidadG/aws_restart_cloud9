"""
Calculadora automatica de 2 numeros
Vamos a solicitar al usuario 2 numeros
y realizar todas las operaciones posibles (+,-,*,/,//,%,**)
mostrando el resultado de una forma clara
"""

# Función para solicitar un número al usuario
def solicitar_n(mensaje): # Se declara la funcion
    while True:
        try:
            return float(input(mensaje)) # Intenta convertir la entrada del usuario a un número flotante
        except ValueError: # Si la conversión falla (es decir, el usuario no ingresó un número válido)
            print("Por favor, ingresa un número válido.") # Muestra un mensaje de error

# Declaramos las variables numericas al mismo tiempo que le pedimos al usuario que las ingrese.
n1 = solicitar_n("Ingresa el primer número: ")
n2 = solicitar_n("Ingresa el segundo número: ")

# Definimos en unas variables nuevas las operaciones que a su ves llaman a las variables n1 y n2.
suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2 if n2 != 0 else "Indefinida (división por cero)"
division_entera = n1 // n2 if n2 != 0 else "Indefinida (división por cero)"
modulo = n1 % n2 if n2 != 0 else "Indefinida (división por cero)"
potencia = n1 ** n2

# Mostrar los resultados llamando a las variales
print("\nResultados:")
print(f"La suma {n1} + {n2} = {suma}")
print(f"La resta {n1} - {n2} = {resta}")
print(f"La multiplicacion {n1} * {n2} = {multiplicacion}")
print(f"La divicion {n1} / {n2} = {division}")
print(f"La divicion entera  {n1} // {n2} = {division_entera}")
print(f"El porcentaje {n1} % {n2} = {modulo}%")
print(f"La potencia de {n1} ** {n2} = {potencia}")
