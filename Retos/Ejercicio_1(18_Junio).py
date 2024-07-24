print(f"Ejercicio 1")
# Solicitar el nombre del usuario
nombre = input("Por favor, ingresa tu nombre: ")

# Solicitar la edad del usuario y convertirla a un número entero
edad = int(input("Por favor, ingresa tu edad: "))

# Calcular la edad del usuario en 5 años
edad_en_5_anos = edad + 5

# Imprimir el mensaje con el resultado
print(f"Hola, {nombre}. En 5 años tendrás {edad_en_5_anos} años.")
print(f"-------------------------------------------------------------")
print(f"Ejercicio 2")
# Crear una lista con los nombres de 5 frutas
frutas = ["manzana", "platano", "frutilla", "naranja", "pera"]
print(f"Se generó una lista de frutas")

# Mostrar el tercer elemento de la lista
tercer_elemento = frutas[2]  # Los índices en Python empiezan en 0, por lo que el tercer elemento está en la posición 2
print("El tercer elemento de la lista es:", tercer_elemento)
print(f"-------------------------------------------------------------")
print(f"Ejercicio 3")
# Solicitar un número entero al usuario
numero = int(input("Por favor, ingresa un número entero: "))

# Determinar si el número es par o impar
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")