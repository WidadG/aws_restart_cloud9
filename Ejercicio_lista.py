"""
Ejercicio lista:
Genera una lista de tu top 5 de canciones favoritas
e imprime la primera y ultima cancion.

"""
top_canciones = [] #Declaro una lista vacia, es en donde se almacenrán las canciones.

# Solicitar al usuario que ingrese sus 5 canciones favoritas
for i in range(5): #para i en el rango de 5 veces
    cancion = input(f"Ingresa la canción #{i+1}: ") #declaro la variable cancion que tendra el valor de lo que ingrese al usuario si el valor de i sea 5
    top_canciones.append(cancion) #con append agregamos la cancion a la lista

# Imprimir la primera y última canción
print("\nPrimera canción:", top_canciones[0])
print("Última canción:", top_canciones[-1])



