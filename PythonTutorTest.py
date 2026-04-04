print("--- DECODIFICADOR DE NOTAS ---")
entrada = int(input("Ingrese la base en la que desea visualizar los datos (2, 8, 10, 16): "))
print("[+] Procesando archivo: notas_dm.txt...")
print("[!] Filtrando ruido místico (valores fuera de rango ASCII)...")#Hare menu creo o puede que lo deje asi

texto = "XYz#84---abc&145*100000!!68mno#111??&171!!!500"#Pequeña muestra
permitido = {"*": "01*","&": "01234567&","#": "0123456789#","!": "0123456789ABCDEF!"}
hexadecimal_numers = {  "A": 10,"B": 11,"C": 12,"D": 13,"E": 14,"F": 15}
hexadecimal_numers2 = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
bases = {"*": 2,"&": 8,"#": 10,"!": 16}
textv3 = []
intermedio = []
conversiones = []
def ignorar_basura(numero): #PRIMER FILTRO
    textv2 = []
    seguro = None #AL PRINCIPIO NO ES NADA, SIRVE PARA DEJAR DE AÑADIR
    temporal = []
    for i in numero:
        if i in permitido:
            prefijo_actual = i  
            temporal = []
            actual = i
            textv2.append(temporal)
            seguro = True
        if seguro:
            if prefijo_actual in permitido[prefijo_actual] and i in permitido[actual]:
                temporal.append(i)
            else:
                seguro = False
    return textv2
filtro = ignorar_basura(texto)

def filtro_ASCII(numero): #Pasa cualquiera prefijo a decimal desde 32 y 126
    for i in numero:
        decimal_total = 0 #Total del decimal
        prefijo = i[0]
        count = 1
        for j in i[1:]:
            if prefijo in permitido[prefijo]:
                count +=1
                if j in hexadecimal_numers:
                    j = hexadecimal_numers[j]
                j = int(j)
                decimal_total += ((bases[prefijo]**(int(len(i))-count)* j))
        if decimal_total >= 32 and decimal_total <= 126:
            textv3.append(i)
            intermedio.append(int(decimal_total)) #Usara intermedio para pasar de decimal a cualquier base
    return textv3
filtro2 = filtro_ASCII(filtro)


def decimal_to_BI_OCT_HEX(numero,base): #Paso de mi lista decimal de arriba a cualquier base ingresada 
    for i in numero: #Mi numero es una lista de decimales en formato int o enteros
        resi = "" #Voy guardando temporalmente transformacion, primero vacio
        while i > 0: #NUmero es mayor que 0
            res = i % base #Lo que va sobrando
            i = i // base #Diviendo y bajando i
            if res in hexadecimal_numers2: #Diccionarios god
                res = hexadecimal_numers2[res] #Diccionarios good
            resi = str(res) + resi #Transforma residuo a str + "", guarda en la derecha y cuando añade va a la izquierda
        print("quepasaca",resi)
        conversiones.append(resi) #Aqui agrego lo guardado temporalmente a una lista que sea usada despues
    return conversiones
decimal_to_BI_OCT_HEX(intermedio,entrada)


indice = 0
for i in range(len(textv3)):
    indice += 1
    print("Valor",str(indice)+ ":" ,conversiones[i], "(Original:", textv3[i],")")


def base_actual_a_ASCII(numero):
    return






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

