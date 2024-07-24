"""
EJERCICIO
Crea una función que te permita hallar el valor del perimetro
dado el área de un círculo

def calcularPerimetro(area):
"""

import math
#Importamos math para ocupar pi de manera exacta, si no, deberiamos declarar una variable con un valor aproximado.


def calcularPerimetro(area):
    # Calcular el radio a partir del área
    radio = math.sqrt(area / math.pi) #Recordar que sqrt es raiz cuadrada
    # Calcular el perímetro
    perimetro = 2 * math.pi * radio
    return perimetro

# Ejemplo de uso
# Pedir al usuario que ingrese el área del círculo
try:
    area_circulo = float(input("Ingrese el área del círculo: "))
    if area_circulo < 0:
        print("El área no puede ser negativa.")
    else:
        perimetro = calcularPerimetro(area_circulo)
        print(f"El perímetro del círculo con área {area_circulo} es: {perimetro:.2f}")
except ValueError:
    print("Por favor, ingrese un número válido.")