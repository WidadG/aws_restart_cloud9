myString = "Esto es una cadena de texto, es decir, un String."
print(myString)
print(type(myString))
print(myString + " es un tipo de dato " + str(type(myString)))
firstString = "auto"
secondString = "pista"
thirdString = firstString + secondString
print(thirdString)
name = input("Cual es tu nombre? ")
print(name)
color = input("Cual es tu color favorito?  ")
animal = input("Cual es tu animal favorito?  ")
print("{}, te gustan cosas el color {} y el {}!".format(name,color,animal))