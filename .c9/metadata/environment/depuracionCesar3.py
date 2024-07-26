{"filter":false,"title":"depuracionCesar3.py","tooltip":"/depuracionCesar3.py","undoManager":{"mark":11,"position":11,"stack":[[{"start":{"row":0,"column":0},"end":{"row":2,"column":3},"action":"insert","lines":["\"\"\"","Ejercicio 2: Trabajo con el programa de cifrado César con errores - Parte 2","\"\"\""],"id":1}],[{"start":{"row":2,"column":3},"end":{"row":2,"column":4},"action":"insert","lines":["s"],"id":2}],[{"start":{"row":2,"column":3},"end":{"row":2,"column":4},"action":"remove","lines":["s"],"id":3}],[{"start":{"row":2,"column":3},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":3,"column":0},"end":{"row":58,"column":30},"action":"insert","lines":["# Módulo Laboratorio: Programa de Cifrado César Error #3","#","# En un laboratorio anterior, creaste un programa de cifrado César. Esta versión del","# programa tiene errores. Usa un depurador para encontrar el error y corregirlo.","","# Duplicar el alfabeto dado","def obtenerAlfabetoDuplicado(alfabeto):","    alfabetoDuplicado = alfabeto + alfabeto","    return alfabetoDuplicado","","# Obtener un mensaje para cifrar","def obtenerMensaje():","    cadenaACifrar = input(\"Por favor, introduce un mensaje para cifrar: \")","    return cadenaACifrar","","# Obtener una clave de cifrado","def obtenerClaveCifrado():","    cantidadDesplazamiento = input(\"Por favor, introduce una clave (número entero del 1 al 25): \")","    return cantidadDesplazamiento","","# Cifrar el mensaje","def cifrarMensaje(mensaje, claveCifrado, alfabeto):","    mensajeCifrado = \"\"","    mensajeMayusculas = \"\"","    mensajeMayusculas = mensaje.upper()","    for caracterActual in mensajeMayusculas:","        posicion = alfabeto.find(caracterActual)","        nuevaPosicion = posicion + int(claveCifrado)","        if caracterActual in alfabeto:","            mensajeCifrado = mensajeCifrado + alfabeto[nuevaPosicion % len(alfabeto)]  # Usar módulo para evitar índices fuera de rango","        else:","            mensajeCifrado = mensajeCifrado + caracterActual","    return mensajeCifrado","","# Descifrar el mensaje","def descifrarMensaje(mensaje, claveCifrado, alfabeto):","    claveDescifrado = -1 * int(claveCifrado)","    return cifrarMensaje(mensaje, str(claveDescifrado), alfabeto)  # Convertir a cadena antes de pasar a cifrarMensaje","","# Lógica principal del programa","def ejecutarProgramaCifradoCesar():","    miAlfabeto = \"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"","    print(f'Alfabeto: {miAlfabeto}')","    miAlfabeto2 = obtenerAlfabetoDuplicado(miAlfabeto)","    print(f'Alfabeto2: {miAlfabeto2}')","    miMensaje = obtenerMensaje()","    print(miMensaje)","    miClaveCifrado = obtenerClaveCifrado()","    print(miClaveCifrado)","    miMensajeCifrado = cifrarMensaje(miMensaje, miClaveCifrado, miAlfabeto2)","    print(f'Mensaje Cifrado: {miMensajeCifrado}')","    miMensajeDescifrado = descifrarMensaje(miMensajeCifrado, miClaveCifrado, miAlfabeto2)","    print(f'Mensaje Descifrado: {miMensajeDescifrado}')","","# Lógica principal","ejecutarProgramaCifradoCesar()"],"id":5}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":75},"action":"remove","lines":["Ejercicio 2: Trabajo con el programa de cifrado César con errores - Parte 2"],"id":6},{"start":{"row":1,"column":0},"end":{"row":1,"column":75},"action":"insert","lines":["Ejercicio 3: Trabajo con el programa de cifrado César con errores - Parte 3"]}],[{"start":{"row":40,"column":34},"end":{"row":40,"column":55},"action":"remove","lines":["str(claveDescifrado),"],"id":7}],[{"start":{"row":40,"column":34},"end":{"row":40,"column":35},"action":"insert","lines":["c"],"id":8},{"start":{"row":40,"column":35},"end":{"row":40,"column":36},"action":"insert","lines":["l"]},{"start":{"row":40,"column":36},"end":{"row":40,"column":37},"action":"insert","lines":["a"]},{"start":{"row":40,"column":37},"end":{"row":40,"column":38},"action":"insert","lines":["v"]},{"start":{"row":40,"column":38},"end":{"row":40,"column":39},"action":"insert","lines":["e"]}],[{"start":{"row":40,"column":39},"end":{"row":40,"column":40},"action":"insert","lines":["C"],"id":9},{"start":{"row":40,"column":40},"end":{"row":40,"column":41},"action":"insert","lines":["i"]},{"start":{"row":40,"column":41},"end":{"row":40,"column":42},"action":"insert","lines":["f"]},{"start":{"row":40,"column":42},"end":{"row":40,"column":43},"action":"insert","lines":["r"]},{"start":{"row":40,"column":43},"end":{"row":40,"column":44},"action":"insert","lines":["a"]},{"start":{"row":40,"column":44},"end":{"row":40,"column":45},"action":"insert","lines":["d"]},{"start":{"row":40,"column":45},"end":{"row":40,"column":46},"action":"insert","lines":["o"]}],[{"start":{"row":40,"column":34},"end":{"row":40,"column":46},"action":"remove","lines":["claveCifrado"],"id":10},{"start":{"row":40,"column":34},"end":{"row":40,"column":46},"action":"insert","lines":["claveCifrado"]}],[{"start":{"row":40,"column":46},"end":{"row":40,"column":47},"action":"insert","lines":[","],"id":11}],[{"start":{"row":40,"column":34},"end":{"row":40,"column":47},"action":"remove","lines":["claveCifrado,"],"id":12},{"start":{"row":40,"column":34},"end":{"row":40,"column":55},"action":"insert","lines":["str(claveDescifrado),"]}]]},"ace":{"folds":[],"scrolltop":743,"scrollleft":0,"selection":{"start":{"row":40,"column":55},"end":{"row":40,"column":55},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":45,"state":"start","mode":"ace/mode/python"}},"timestamp":1722011630494,"hash":"a79b1fcdecaf384f7e02e5105f72b715db4ff3bc"}