userReply = input("Nececitas enviar un paquete? (Ingrese si o no) ") #Le pedimos al usuario una respuesta

if userReply == "si": #Si la respuesta del usuario es igual a si
    print("Podemos ayudarte a enviar ese paquete!") #Aplicamos un if para cierta respuesta ingresada por el usuario.
    
else: #Si no...
    print("Vuelve cuando quieras enviar un paquete, muchas gracias.") #Else automatimente asume cualquier otra respuesta que no este incluida en el if anterior.
    

#Elif es para varias condiciones y siempre va despues un if.
userReply = input("Te gustaria comprar estampillas, un sobre, o hacer una copia? (Ingresa estampillas, sobre, o copia) ")
if userReply == "estampilla":
    print("Tenemos muchos diseños para que puedas elegir.")
elif userReply == "sobre":
    print("Tenemos diferentes tamaños para que puedas elegir.")
elif userReply == "copia":
    copies = input("Cuantas copias quieres? (Ingresa un numero) ")
    print("tenemos {} copias disponibles.".format(copies))
else:
    print("Gracias, vuelve pronto.")