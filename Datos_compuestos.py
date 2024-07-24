import csv  #Con esto importo el archivo donde esta el inventario.
import copy

myVehicle = { #Con esto se leeran los datos
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "modelo" : "<empty>" ,
    "anio" : 0,        #Inicializa en 0
    "rango" : 0,
    "velocidadMaxima" : 0,
    "zeroSixty" : 0.0,
    "millas" : 0
}

for key, value in myVehicle.items(): #Es un for para recorrer vyVehicle
    print("{} : {}".format(key,value))
    
myInventoryList = [] #Se define una lista vacia que almacenará lo que se lea antes.

with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0  
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, modelo: {row[2]}, anio: {row[3]}, rango: {row[4]}, velocidadMaxima: {row[5]}, zeroSixty: {row[6]}, millas: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["modelo"] = row[2]  
            currentVehicle["anio"] = row[3]  
            currentVehicle["rango"] = row[4]  
            currentVehicle["velocidadMaxima"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["millas"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')
    
    currentVehicle = copy.deepcopy(myVehicle)
    
    for myCarProperties in myInventoryList:
        for key, value in myCarProperties.items():
            print("{} : {}".format(key,value))
            print("-----")
        
