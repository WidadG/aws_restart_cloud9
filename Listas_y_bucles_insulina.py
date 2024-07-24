# Python3.8  
# Coding: utf-8  
# Store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulina = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  
# Store the remaining sequence elements of human insulin in variables:  
sInsulina= "malwmrllpllallalwgpdpaaa" # Secuencia de señal: aminoácidos 1-24
bInsulina = "fvnqhlcgshlvealylvcgergffytpkt"  # Cadena B de insulina: aminoácidos 25-54
pep_cInsulina = "rreaedlqvgqvelgggpgagslqplalegslqkr" # Péptido C: aminoácidos 55-89
aInsulina = "giveqcctsicslyqlenycn"
insulina = preproInsulina[24:54] + preproInsulina[89:110]

"""
Ejercicio 1: Asignación de variables, listas y diccionarios
"""
# Crear el diccionario pKR con los valores especificados
pKR = {
    'y': 10.07,
    'c': 8.18,
    'k': 10.53,
    'h': 6.00,
    'r': 12.48,
    'd': 3.65,
    'e': 4.25
}

# Imprimir el diccionario pKR para verificar su contenido
print("Los valores de pKa (o pKr) para ciertos aminoácidos: ", pKR)

"""
Ejercicio 2: Asignación de variables, listas y diccionarios
"""
# Contar la cantidad de aminoácidos Y, C, K, H, R, D y E en la insulina
seqCount = {x: float(insulina.count(x.upper())) for x in ['y', 'c', 'k', 'h', 'r', 'd', 'e']}

print("Conteo de Aminoácidos en Insulina: ", seqCount)

"""
Ejercicio 3: Escritura de la fórmula de la carga neta
"""

# Calcular y mostrar la carga neta en función del pH
pH = 0
while pH <= 14:
    cargaNeta = (
        +(sum((seqCount[x] * (10 ** pKR[x])) / ((10 ** pH) + (10 ** pKR[x])) for x in ['k', 'h', 'r']))
        - (sum((seqCount[x] * (10 ** pH)) / ((10 ** pH) + (10 ** pKR[x])) for x in ['y', 'c', 'd', 'e']))
    )
    print("La carga neta del pH es:")
    print('{0:.2f}'.format(pH), cargaNeta)
    pH += 1