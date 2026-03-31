#Programa que transforma dependiendo del caso a binario, octal, decimal y hexadecimal

file = open("Encriptados/prueba_1.txt", "r")
texto = file.read()

textv2 = [] #Texto limpio con los filtros ya aplicados
busca = "" #Buscando los prefijos
copia = False #Para que no copie de una, sino bajo una condicion, apagado al comenzar

"""""
for letra in texto:

    if letra == "#" or letra == "*" or letra == "&":
        copia = True
    elif letra not in ("0123456789"):
        copia = False
    if copia:
        textv2.append(letra)
"""""


for letra in texto: #Ciclo for
    if letra == "#" or letra == "*" or letra == "&" or letra == "!": #Condicion que se va a buscar
        copia = True #Copia se activa y empieza a duplicar digamos hasta que se vuelva False
        busca = letra #Lo que se esta buscando y funcionara como condicional
    if copia:#Si es True
        if busca == "#" and letra not in ("012345678#"):#Si el prefijo es True y la letra no esta en ese mini diccionario, es True, da True y deja de copiar al ponerlo en False.
            copia = False #Deja de copiar
        elif busca == "*" and letra not in ("01*"):#Si el prefijo es True y la letra no esta en ese mini diccionario, es True, da True y deja de copiar al ponerlo en False.
            copia = False #Deja de copiar
        elif busca == "&" and letra not in ("01234567&"):#Si el prefijo es True y la letra no esta en ese mini diccionario, es True, da True y deja de copiar al ponerlo en False.
            copia = False #Deja de copiar
        elif busca == "!" and letra not in ("0123456789ABCDEF!"):#Si el prefijo es True y la letra no esta en ese mini diccionario, es True, da True y deja de copiar al ponerlo en False.
            copia = False #Deja de copiar
    if copia:#Si es True
        textv2.append(letra)#Va agregando a la nueva version


print(texto)
print(textv2)
file.close()