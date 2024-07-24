import random

print("Bienvenidos a Adivina el numero!")
print("Las reglas son simples. Pensaré en un numero y tú tratarás de adivinarlo.")

number = random.randint(1,10)#Busca un numero al azar entre 1 y 10.

isGuessRight = False #Declaracion de la variable partiendo del estado falso.
#Parte del estado falso porque si es verdadero no podía comenzar el siclo siquiera.

while isGuessRight != True: #Mientras la funcion sea distinta a verdadera
    guess = input("Adivina un numero entre 1 y 10: ") #Se declara la variable en la que se le pide al usuario que ingrese el valor.
    if int(guess) == number: #Si el contenido de esta variable es igual a la variable que fue antes declarada con la funcion random para dar un numero al azar
        print("Tu suposicion fue {}. Es correcto, tu ganas!".format(guess))
        isGuessRight = True #Si la variable pasa a verdadero, el ciclo se detiene...
    else: #si no...
        print("Tu suposicion fue {}. Lo siento pero no acertaste. Intenta de nuevo.".format(guess))

