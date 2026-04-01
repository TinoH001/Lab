#Programa que transforma dependiendo del caso a binario, octal, decimal y hexadecimal

file = open("Encriptados/prueba_1.txt", "r")
texto = file.read()

textv2 = [] #Texto limpio con los filtros ya aplicados
prefijo_buscar = "" #Buscando los prefijos
copia = False #Para que no copie de una, sino bajo una condicion, apagado al comenzar
""""
for letra in texto:

    if letra == "#" or letra == "*" or letra == "&":
        copia = True
    elif letra not in ("0123456789"):
        copia = False
    if copia:
        textv2.append(letra)
"""""

temporal = "" #Temporal que va a ser agregado como lista al texto limpio
for letra in texto: #Ciclo for
    if letra == "*" or letra == "#" or letra == "&" or letra == "!": #Condicion que se va a buscar
        if temporal != "": #Si tengo algo en mi temporal incluyendo al prefijo es True
            textv2.append(temporal) #Agrego a mi textov2
        copia = True #Empezamos a copiar
        prefijo_buscar = letra #Cambio prefijo_buscar al prefijo, esto me permitira acceder a las condiconales de abajo
        temporal = "" #Limpiamos temporal una vez ya agregado arriba sino se va a agregar de mala forma
    if copia:
        if prefijo_buscar == "#" and letra not in ("0123456789#"):#Si el prefijo es True y la letra no esta en ese mini diccionario, es True, da True y deja de copiar al ponerlo en False.
            copia = False#Deja de copiar
        elif prefijo_buscar == "*" and letra not in ("01*"):#Si el prefijo es True y la letra no esta en ese mini diccionario, es True, da True y deja de copiar al ponerlo en False.
            copia = False#Deja de copiar
        elif prefijo_buscar == "&" and letra not in ("01234567&"):#Si el prefijo es True y la letra no esta en ese mini diccionario, es True, da True y deja de copiar al ponerlo en False.
            copia = False#Deja de copiar
        elif prefijo_buscar == "!" and letra not in ("0123456789ABCDEF!"):#Si el prefijo es True y la letra no esta en ese mini diccionario, es True, da True y deja de copiar al ponerlo en False.
            copia = False#Deja de copiar
    if copia: 
        temporal += letra #Añade a temporal el numero o letra del momento
    else: #False
        if temporal != "":#Sirve para saber si aun tiene String en temporal o esta vacio
            textv2.append(temporal)#Si tiene lo agrega al textov2
            temporal = ""#Reinicia a 0
textv2.append(temporal)#Esto es un seguro para ultimo dato guardado
print(texto)
print(textv2)
file.close()