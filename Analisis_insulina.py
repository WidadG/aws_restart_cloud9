# Leer la secuencia de preproinsulina desde el archivo
with open('preproinsulina-seq_clean.txt', 'r') as file:
    sequence = file.read().strip()

# Verificar que la secuencia tenga 110 caracteres
# Para esto usaremos la funcion raise. raise [variable de escepcion[, mensaje]]
# Con la funcion len podemos saber la cantidad de caracteres en una variable.
if len(sequence) != 110: 
    raise ValueError(f"Error: La secuencia tiene {len(sequence)} caracteres, se esperaban 110.")
else:
    print("Secuencia de preproinsulina leída correctamente. Longitud verificada: 110 caracteres.")
    
# Extraer las diferentes partes de la secuencia
# Segun el enunciado sabemos que La preproinsulina contiene una secuencia de señal 24aa y una molécula de proinsulina 86aa. 
# Los aminoácidos 25–54 y los aminoácidos 90–110 son la molécula de la insulina procesada
senial_secuencia = sequence[0:24]  # Secuencia de señal: aminoácidos 1-24
cadena_b_in_secuencia = sequence[24:54]  # Cadena B de insulina: aminoácidos 25-54
peptido_c_in_secuencia = sequence[54:89]  # Péptido C: aminoácidos 55-89
cadena_a_in_secuencia = sequence[89:110]  # Cadena A de insulina: aminoácidos 90-110

# Guardar las secuencias en archivos separados y verificar la longitud
with open('Secuencia_de_señal_clean.txt', 'w') as file:
    file.write(senial_secuencia)
if len(senial_secuencia) != 24:
    raise ValueError(f"Error: lsinsulin-seq_clean.txt tiene {len(senial_secuencia)} caracteres, se esperaban 24.")
else:
    print("Secuencia_de_señal_clean.txt guardado correctamente. Longitud verificada: 24 caracteres.")

with open('Cadena_B_de_insulina_clean.txt', 'w') as file:
    file.write(cadena_b_in_secuencia)
if len(cadena_b_in_secuencia) != 30:
    raise ValueError(f"Error: binsulin-seq_clean.txt tiene {len(cadena_b_in_secuencia)} caracteres, se esperaban 30.")
else:
    print("Cadena_B_de_insulina_clean.txt guardado correctamente. Longitud verificada: 30 caracteres.")

with open('Péptido_C_insulina_clean.txt', 'w') as file:
    file.write(peptido_c_in_secuencia)
if len(peptido_c_in_secuencia) != 35:
    raise ValueError(f"Error: cinsulin-seq_clean.txt tiene {len(peptido_c_in_secuencia)} caracteres, se esperaban 35.")
else:
    print("Péptido_C_insulina_clean.txt guardado correctamente. Longitud verificada: 35 caracteres.")

with open('Cadena_A_de_insulina_clean.txt', 'w') as file:
    file.write(cadena_a_in_secuencia)
if len(cadena_a_in_secuencia) != 21:
    raise ValueError(f"Error: Cadena_A_de_insulina_clean.txt tiene {len(cadena_a_in_secuencia)} caracteres, se esperaban 21.")
else:
    print("ainsulin-seq-clean.txt guardado correctamente. Longitud verificada: 21 caracteres.")