print(f"Ejercicio 1")
# Solicitar dos números al usuario
n1 = int(input("Por favor, ingresa el primer número: "))
n2 = int(input("Por favor, ingresa el segundo número: "))

# Verificar si ambos números son positivos
if n1 > 0 and n2 > 0:
    print("Ambos números son positivos.")
else:
    print("Uno o ambos números no son positivos.")
    
print(f"-------------------------------------------------------------")
print(f"Ejercicio 2")    
def id_valida(identificacion):
    # Verificar si la identificación es numérica y tiene 9 dígitos
    return identificacion.isdigit() and len(identificacion) == 9

try:
    # Solicitar la edad del usuario
    edad = int(input("Por favor, ingresa tu edad: "))

    # Solicitar la identificación del usuario
    identificacion = input("Por favor, ingresa tu identificación: ").strip()

    # Verificar si la persona es mayor de 18 años y tiene una identificación válida
    if edad >= 18 and id_valida(identificacion):
        print("Eres apto para votar.")
    else:
        if edad < 18:
            print("No eres apto para votar porque no tienes la edad suficiente.")
        if not id_valida(identificacion):
            print("No eres apto para votar porque tu identificación no es válida.")
except ValueError:
    print("Por favor, ingresa una identificacion valida.")