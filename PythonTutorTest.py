
texto = "*0001!F21&112!41_LX#74&1PyLKvGr#74&1557&1417!41iWW+uNj#835#46"#Pequeña muestra
textv2 = []
copia = False 
temporal = []
binary = "01*"
octal = "01234567&"
decimal = "0123456789#"
hexadecimal = "0123456789ABCDEF!"
bases = "*", "#", "&", "!"
for letra in texto: #
    if letra in bases:
        if temporal != []:
            textv2.append(temporal)
        copia = True
        prefijo_buscar = letra
        temporal = []
    if copia:#MUCHO IF, QUIZAS USE DICCIONARIO Y SOLO 1 IF
        if prefijo_buscar == "#" and letra not in decimal:
            copia = False
        elif prefijo_buscar == "*" and letra not in binary:
            copia = False
        elif prefijo_buscar == "&" and letra not in octal:
            copia = False
        elif prefijo_buscar == "!" and letra not in hexadecimal:
            copia = False
    if copia:
        temporal += letra
    else:
        if temporal != []: 
            textv2.append(temporal)
            temporal = []
textv2.append(temporal)

"""""
def base_x_to_base_decimal(numero):
    f = 0
    for i in numero:
        prefijo = i[0]
        count = 1
        for j in i[1:]:
            j = int(j)
            print(j)
            print(type(j))
            if prefijo == "*":
                count +=1
                
                indice = (int(len(i))-count)
                print("Indice: ", indice, "---  Numero actual:", j)
                k = int((2**indice))
                k = j* k
                f += k
                print("Por ahora", f)
    print("Transformado a decimal solo para binario:",f)
base_x_to_base_decimal(textv2)

"""""
textv3 = [] #FULL FILTROX
#32 y 126 rango permitido para decimales ya transformados
hexadecimal_numers = {  
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15
}
def base_x_to_base_decimal(numero):
    extra = 0 #EXTRA PARA SABER SI VOY BIEN ENCAMINADO
    for i in numero:
        f = 0 #LA SUMA DE TOTAL DECIMAL
        prefijo = i[0] #TOMAMOS PREFIJO A PARTIR DEL INDICE 0 DE LA LISTA
        count = 1 #FUI INTENTANDO (+-) Y ESTE FUNCIONAXD, USARE PARA RESTAR POR EL LEN DEL LA LISTA DEL PREFIJO COMENZANDO POR 1 Y NO 0
       
        #ESTO SE PUEDE HACER CON UN SOLO 1 IF CREO SI USO DICCIONARIO PARA SACAR LA BASE Y EL PREFIJO
        ######################################################################################
        for j in i[1:]: #TOMO LOS VALORES DESPUES DEL PREFIJO
            if prefijo == "#": #
                j = int(j) #CONVIERTO A INT PARA TRABAJARLO 
                k = 0 #REINICIAR A 0 Y QUE NO SE ACUMULE
                count +=1 #SUMO 1 POR CADA RECORRIDO DENTRO DE LA LISTA DESPUES DEL PREFIJO, DERECHA A IZQUIERDA
                k = (10**(int(len(i))-count)*j)#OCURRE LA MAGIA, LARGO DE LA LISTA SE VA A IR RESTANDO POR LA CANTIDAD DE ITERACIONES, AL FINAL SERA 0
                f += k #SUMO A MI TOTAL DECIMAL DE A POCO HASTA ACABAR
            elif prefijo == "*":
                j = int(j)
                k = 0
                count +=1
                k = (2**(int(len(i))-count)*j)
                f += k
            elif prefijo == "&":
                j = int(j)
                k = 0
                count +=1
                k = (8**(int(len(i))-count)*j)
                f += k
            else: #SI NO TOMA ALGUNO DE ARRIBA TOCA HEXADECIMAL
                k = 0
                count +=1
                if j in hexadecimal_numers: #USANDO IF PARA IR AL DICCIONARIO Y REEMPLAZAR LA LETRA POR EL NUMERO CORRESPONDIENTE
                    j = hexadecimal_numers[j]
                j = int(j) 
                k = (16**(int(len(i))-count)* j)
                f += k
        if f >= 32 and f <= 126: #FILTRO DE ASCII Y SE AÑADE A LA NUEVA LISTA v3, LAS PERMITIDAS
            print("Esta dentro del rango permitido:", f,"            lista con prefijo: ",i)
            textv3.append(i)
            extra+=1
            print("total de permitidos",extra)
    print("veamos",len(textv3))
        
       

base_x_to_base_decimal(textv2)

print("Antes filtro decimal: ", textv2)
print("Despues del filtro decimal: ", textv3)

#NO ME GUSTA QUE TENGA 2 VERSIONES EXTRAS DE LA ORIGINAL, QUIZAS LO PUEDA HACER A 1
#PONDRE AMBOS FOR DENTRO DE UN MISMO DEF Y USARE DICCIONARIO PARA REDUCIR LOS IF Y DEJARLO MÁS LIMPIO