# La versión de Python (python3.8) con una ruta al archivo ejecutable, si es posible
# La codificación del archivo (normalmente, coding: utf-8)

# Almacenar la secuencia de preproinsulina humana en una variable llamada preproinsulina
preproInsulina= "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
                "reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Almacenar los elementos de secuencia restantes de la insulina humana en variables
sInsulina= "malwmrllpllallalwgpdpaaa" # Secuencia de señal: aminoácidos 1-24
bInsulina = "fvnqhlcgshlvealylvcgergffytpkt"  # Cadena B de insulina: aminoácidos 25-54
pep_cInsulina = "rreaedlqvgqvelgggpgagslqplalegslqkr" # Péptido C: aminoácidos 55-89
aInsulina = "giveqcctsicslyqlenycn"

# Imprimir "la secuencia de insulina humana" en la consola utilizando comandos print() sucesivos
print("La secuencia de la preinsulina humana es:")
print(preproInsulina)

# Imprimir en la consola usando cadenas concatenadas dentro de la función print (una sola línea)
print("La secuencia de la preinsulina humana es, cadena a: " + aInsulina)

# Se extraen las cadenas B y A de la secuencia de preproinsulina para formar la insulina activa.
insulina = preproInsulina[24:54] + preproInsulina[89:110]

# Calculando el peso molecular de la insulina
# Creando una lista de los pesos de los aminoácidos (AA)
aaPesos = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}  
# Contar el número de cada aminoácido (aa)
aaCountInsulina = ({x: float(insulina.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']})  
# Multiplicar el conteo por los pesos 
pesoMolecularInsulina = sum({x: (aaCountInsulina[x]*aaPesos[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())  
print("El peso molecular aproximado de la insulina es de: " + str(pesoMolecularInsulina))

pesoMolecularInsulinaActual = 5807.63
print("Error percentage: " + str(((pesoMolecularInsulina - pesoMolecularInsulinaActual)/pesoMolecularInsulinaActual)*100))
