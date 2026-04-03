texto = "*0001!F21&112!41_LX#74&1PyLKvGr#74&1557&1417!41iWW+uNj#835#46"#Pequeña muestra
permitido = {"*": "01*","&": "01234567&","#": "0123456789#","!": "0123456789ABCDEF!"}
textv2 = []
seguro = False #MI SEGURO PARA DEJE DE AÑADIR
for letra in texto: #LINDOS LOS DICCIONARIOS
    if letra in permitido:
        prefijo_buscar = letra
        temporal = [] #REINICIA 0
        actual = letra #CAMBIANDO DE ESTADO Y SIRVE PARA CONFIRMAR DENTRO DEL DICCIONARIO
        textv2.append(temporal)#AÑADE A MI NUEVA VERSION LIMPIA
        seguro = True 
    if seguro: #SOLO AÑADE SI ES TRUE
        if prefijo_buscar in permitido[prefijo_buscar] and letra in permitido[actual]: #SE CUMPLE QUE MI PREFIJO ESTA EN PREFIJO_BUSCAR Y LA LETRA ACTUAL DENTRO DEL RANGO PERMITIDO ES TRUE
            temporal.append(letra)#AÑADE A MI LISTA TEMPORAL
        else:
            seguro = False #DEJA DE AÑADIR AL PASAR A ESTADO FALSE
print(textv2)



textv3 = [] #FULL FILTROX
#32 y 126 rango permitido para decimales ya transformados
hexadecimal_numers = {  "A": 10,"B": 11,"C": 12,"D": 13,"E": 14,"F": 15}
bases = {"*": 2,"&": 8,"#": 10,"!": 16}
def base_x_to_base_decimal(numero):
    extra = 0 #EXTRA PARA SABER SI VOY BIEN ENCAMINADO
    for i in numero:
        f = 0 #LA SUMA DE TOTAL DECIMAL
        prefijo = i[0] #TOMAMOS PREFIJO A PARTIR DEL INDICE 0 DE LA LISTA
        count = 1 #FUI INTENTANDO (+-) Y ESTE FUNCIONAXD, USARE PARA RESTAR POR EL LEN DEL LA LISTA DEL PREFIJO COMENZANDO POR 1 Y NO 0
        for j in i[1:]: #TOMO LOS VALORES DESPUES DEL PREFIJO
            if prefijo in permitido[prefijo]: 
                k = 0
                count +=1
                if j in hexadecimal_numers: #USANDO IF PARA IR AL DICCIONARIO Y REEMPLAZAR LA LETRA POR EL NUMERO CORRESPONDIENTE
                    j = hexadecimal_numers[j]
                j = int(j) 
                k = (bases[prefijo]**(int(len(i))-count)* j)
                f += k
        if f >= 32 and f <= 126: #FILTRO DE ASCII Y SE AÑADE A LA NUEVA LISTA v3, LAS PERMITIDAS
            print("Esta dentro del rango permitido:", f,"            lista con prefijo: ",i)
            textv3.append(i)
            extra+=1
            print("total de permitidos",extra)
        
base_x_to_base_decimal(textv2)
print(textv2)
print("Despues del filtro decimal: ", len(textv3))
print(textv3)
#Unire ambos for dentro de un def para el filtrox

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
#NO ME GUSTA QUE TENGA 2 VERSIONES EXTRAS DE LA ORIGINAL, QUIZAS LO PUEDA HACER A 1
#PONDRE AMBOS FOR DENTRO DE UN MISMO DEF Y USARE DICCIONARIO PARA REDUCIR LOS IF Y DEJARLO MÁS LIMPIO

