"""
Ejercicio 3: Creación del programa principal
"""

import Controladores_de_archivos

datos = Controladores_de_archivos.leerJsonFile('/home/ec2-user/environment/insulina.json')

if datos != "":
    sInsulina = datos['molecular']['sInsulina']
    bInsulina = datos['molecular']['bInsulina']
    aInsulina = datos['molecular']['aInsulina']
    pep_cInsulina = datos['molecular']['pep_cInsulina']
    insulina = bInsulina + aInsulina
    pesoMolecularInsulinaActual = datos['pesoMolecularInsulinaActual']
    print('sInsulina: ' + sInsulina)
    print('bInsulina: ' + bInsulina)
    print('aInsulina: ' + aInsulina)
    print('pep_cInsulina: ' + pep_cInsulina)
    print('pesoMolecularInsulinaActual: ' + str(pesoMolecularInsulinaActual))
else:
    print("Error. Exiting program")
    
# Calculando el peso molecular de la insulina  
# Lista de aminoácidos 
aaPesos = datos['pesos']
# Contador de aminoácidos
aaCountInsulina = ({x: float(insulina.upper().count(x)) for x in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']})  
# Multiplicador del contador por el peso
pesoMolecularInsulina = sum({x: (aaCountInsulina[x]*aaPesos[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']}.values())  
print("El peso molecular aproximado de la insulina: " + str(pesoMolecularInsulina))
print("Porcentaje de error: " + str(((pesoMolecularInsulina - pesoMolecularInsulinaActual)/pesoMolecularInsulinaActual)*100))