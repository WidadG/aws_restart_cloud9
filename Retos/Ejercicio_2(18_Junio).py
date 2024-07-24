print(f"Ejercicio 1")
# Solicitar el nombre del usuario
nombre = input("Por favor, ingresa tu nombre: ")

# Solicitar la edad del usuario y convertirla a un número entero
edad = int(input("Por favor, ingresa tu edad: "))

# Determinar si el usuario puede votar
if edad >= 18:
    print(f"Genial {nombre}. Tienes la edad suficiente para votar.")
else:
    print(f"Lo siento {nombre}. No tienes la edad suficiente para votar.")

print(f"-------------------------------------------------------------")
# Solicitar la temperatura en grados Celsius al usuario
temperatura = float(input("Por favor, ingresa la temperatura en grados Celsius: "))

# Determinar el estado del agua
if temperatura <= 0:
    estado = "sólido"
elif temperatura >= 100:
    estado = "gaseoso"
else:
    estado = "líquido"

# Imprimir el resultado
print(f"A {temperatura} grados Celsius, el agua está en estado {estado}.")
print(f"-------------------------------------------------------------")
print(f"Ejercicio 3")
# Solicitar un número entero al usuario
numero = int(input("Por favor, ingresa un número entero: "))

# Determinar si el número es positivo, negativo o cero
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
