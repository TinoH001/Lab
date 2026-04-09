ascii_dict = {
    #    dec   hex    oct    bin
    " ": [32,  "20",  40,  100000],
    "!": [33,  "21",  41,  100001],
    '"': [34,  "22",  42,  100010],
    "#": [35,  "23",  43,  100011],
    "$": [36,  "24",  44,  100100],
    "%": [37,  "25",  45,  100101],
    "&": [38,  "26",  46,  100110],
    "'": [39,  "27",  47,  100111],
    "(": [40,  "28",  50,  101000],
    ")": [41,  "29",  51,  101001],
    "*": [42,  "2A",  52,  101010],
    "+": [43,  "2B",  53,  101011],
    ",": [44,  "2C",  54,  101100],
    "-": [45,  "2D",  55,  101101],
    ".": [46,  "2E",  56,  101110],
    "/": [47,  "2F",  57,  101111],
    "0": [48,  "30",  60,  110000],
    "1": [49,  "31",  61,  110001],
    "2": [50,  "32",  62,  110010],
    "3": [51,  "33",  63,  110011],
    "4": [52,  "34",  64,  110100],
    "5": [53,  "35",  65,  110101],
    "6": [54,  "36",  66,  110110],
    "7": [55,  "37",  67,  110111],
    "8": [56,  "38",  70,  111000],
    "9": [57,  "39",  71,  111001],
    ":": [58,  "3A",  72,  111010],
    ";": [59,  "3B",  73,  111011],
    "<": [60,  "3C",  74,  111100],
    "=": [61,  "3D",  75,  111101],
    ">": [62,  "3E",  76,  111110],
    "?": [63,  "3F",  77,  111111],
    "@": [64,  "40", 100, 1000000],
    "A": [65,  "41", 101, 1000001],
    "B": [66,  "42", 102, 1000010],
    "C": [67,  "43", 103, 1000011],
    "D": [68,  "44", 104, 1000100],
    "E": [69,  "45", 105, 1000101],
    "F": [70,  "46", 106, 1000110],
    "G": [71,  "47", 107, 1000111],
    "H": [72,  "48", 110, 1001000],
    "I": [73,  "49", 111, 1001001],
    "J": [74,  "4A", 112, 1001010],
    "K": [75,  "4B", 113, 1001011],
    "L": [76,  "4C", 114, 1001100],
    "M": [77,  "4D", 115, 1001101],
    "N": [78,  "4E", 116, 1001110],
    "O": [79,  "4F", 117, 1001111],
    "P": [80,  "50", 120, 1010000],
    "Q": [81,  "51", 121, 1010001],
    "R": [82,  "52", 122, 1010010],
    "S": [83,  "53", 123, 1010011],
    "T": [84,  "54", 124, 1010100],
    "U": [85,  "55", 125, 1010101],
    "V": [86,  "56", 126, 1010110],
    "W": [87,  "57", 127, 1010111],
    "X": [88,  "58", 130, 1011000],
    "Y": [89,  "59", 131, 1011001],
    "Z": [90,  "5A", 132, 1011010],
    "[": [91,  "5B", 133, 1011011],
    "\\": [92, "5C", 134, 1011100],
    "]": [93,  "5D", 135, 1011101],
    "^": [94,  "5E", 136, 1011110],
    "_": [95,  "5F", 137, 1011111],
    "`": [96,  "60", 140, 1100000],
    "a": [97,  "61", 141, 1100001],
    "b": [98,  "62", 142, 1100010],
    "c": [99,  "63", 143, 1100011],
    "d": [100, "64", 144, 1100100],
    "e": [101, "65", 145, 1100101],
    "f": [102, "66", 146, 1100110],
    "g": [103, "67", 147, 1100111],
    "h": [104, "68", 150, 1101000],
    "i": [105, "69", 151, 1101001],
    "j": [106, "6A", 152, 1101010],
    "k": [107, "6B", 153, 1101011],
    "l": [108, "6C", 154, 1101100],
    "m": [109, "6D", 155, 1101101],
    "n": [110, "6E", 156, 1101110],
    "o": [111, "6F", 157, 1101111],
    "p": [112, "70", 160, 1110000],
    "q": [113, "71", 161, 1110001],
    "r": [114, "72", 162, 1110010],
    "s": [115, "73", 163, 1110011],
    "t": [116, "74", 164, 1110100],
    "u": [117, "75", 165, 1110101],
    "v": [118, "76", 166, 1110110],
    "w": [119, "77", 167, 1110111],
    "x": [120, "78", 170, 1111000],
    "y": [121, "79", 171, 1111001],
    "z": [122, "7A", 172, 1111010],
    "{": [123, "7B", 173, 1111011],
    "|": [124, "7C", 174, 1111100],
    "}": [125, "7D", 175, 1111101],
    "~": [126, "7E", 176, 1111110],
}

permitido = {"*": "01*","&": "01234567&","#": "0123456789#","!": "0123456789ABCDEF!"}
Prefijo_to_base = {"*": 2,"&": 8,"#": 10,"!": 16, 2: "*", 8: "&", 10: "#", 16: "!"}
hexadecimal_numbers = {"A": 10,"B": 11,"C": 12,"D": 13,"E": 14,"F": 15, 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

def leer(nombre_archivo): #Leer archivo y sacar nombre del .txt
    archivo=open(nombre_archivo,'r')
    texto = archivo.read()
    archivo_nombre = nombre_archivo.split("/")[-1]
    archivo.close()
    return texto,archivo_nombre

def ignorar_basura(numero): #Ignorar los no prefijos y no permitidos
    version_2 = []
    seguro = None #AL PRINCIPIO NO ES NADA, SIRVE PARA DEJAR DE AÑADIR
    temporal = ""
    for i in numero:
        if i in permitido:
            prefijo_actual = i  
            temporal = []
            actual = i
            version_2.append(temporal)
            seguro = True
        if seguro:
            if prefijo_actual in permitido[prefijo_actual] and i in permitido[actual]:
                temporal.append(i)
            else:
                seguro = False
    return version_2

def BaseX_to_decimal(numero): #Pasa cualquiera prefijo a decimal desde 32 y 126
    version_3 = []
    intermedio = []
    for i in numero:
        decimal_total = 0 #Total del decimal
        prefijo = i[0]
        count = 1
        for j in i[1:]:
            if prefijo in permitido[prefijo]:
                count +=1
                if j in hexadecimal_numbers:
                    j = hexadecimal_numbers[j]
                j = int(j)
                decimal_total += ((Prefijo_to_base[prefijo]**(int(len(i))-count)* j))
        if decimal_total >= 32 and decimal_total <= 126:
            version_3.append(i)
            intermedio.append(int(decimal_total)) #Usara intermedio para pasar de decimal a cualquier base
    return version_3, intermedio

def decimal_to_BI_OCT_HEX(numero,base): #Paso de mi lista decimal de arriba a cualquier base ingresada 
    conversiones = []
    for i in numero: #Mi numero es una lista de decimales en formato int o enteros
        resi = "" #Voy guardando temporalmente transformacion, primero vacio
        while i > 0: #NUmero es mayor que 0
            res = i % base #Lo que va sobrando
            i = i // base #Diviendo y bajando i
            if res in hexadecimal_numbers: #Diccionarios god
                res = hexadecimal_numbers[res] #Diccionarios good
            resi = str(res) + resi #Transforma residuo a str + "", guarda en la derecha y cuando añade va a la izquierda
        conversiones.append(resi) #Aqui agrego lo guardado temporalmente a una lista que sea usada despues
    return conversiones

def base_actual_a_ASCII(prefijo,numeros,diccionario):#Entrada Base, conversiones sin prefijo, diccionario completo
    texto_completo = "" #Texto completo que sera reutilizado para un output
    if prefijo == 2: 
        seleccionar_base = 3 #Indice dentro del diccionario Ascii
    elif prefijo == 8:
        seleccionar_base = 2
    elif prefijo == 10:
        seleccionar_base = 0
    elif prefijo == 16:
        seleccionar_base = 1
    else:
        print("Error, base no encontrada en el dicionarrio")
    for i in numeros: #Recorro la lista sin prefijos ya transformado a la base correspondiente
        for j,k in diccionario.items(): #j, k son caracter y base, digamos seria A y hexadecimal 10
            if str(k[seleccionar_base]) == i:#Toma valor de la base, al ser hexa o deci y lo compara con el numero actual para saber si esta, en caso de ser asi se agregara ese caracter j
                texto_completo += str(j)
    return texto_completo

def printeo(lista1,list2,texto,entrada,archivo_nombre):
    nombre_del_prefijo = [] #Los nombres de los prefijos para usarlos despues
    for i in lista1:
        prefijo = i[0]
        if prefijo == "*":
            nombre_del_prefijo.append("Binario")
        elif prefijo == "&":
            nombre_del_prefijo.append("Octal")
        elif prefijo == "#":
            nombre_del_prefijo.append("Decimal")
        elif prefijo == "!":
            nombre_del_prefijo.append("Hexadecimal")
        else:
            nombre_del_prefijo.append(prefijo)
    print("")
    print("[+] Procesando archivo: ", archivo_nombre, "...")
    print("[!] Filtrando ruido místico (valores fuera de rango ASCII)...\n "" ")#Hare menu creo o puede que lo deje asi
    print("LISTA DE VALORES EXTRAÍDOS (Base "+ str(entrada)+"): " + "\n--------------------------------------------------")
    print("[Proceso finalizado con éxito]")
    indice = 0 
    for i in range(len(lista1)): #Rango de version_v3
        indice += 1
        print("Valor",str(indice)+ ":" ,list2[i],"(Original:",nombre_del_prefijo[i],"".join(lista1[i]) + ")")
    print("--------------------------------------------------""\n""\nMENSAJE DECODIFICADO:")
    print(texto,"\n" "\n[Proceso finalizado con éxito]")
    return

def main():
    print("             --- DECODIFICADOR DE NOTAS --- \n "" \n "" ") 
    entrada = int(input("Ingrese la base en la que desea visualizar los datos (2, 8, 10, 16): ")) 
    if entrada == 2 or entrada == 8 or entrada == 10 or entrada == 16: #Solo va a dejar las bases correspondientes
        pass
    else:
        print("Base incorrecta, vuelve a intentar")
        return
    
    texto,archivo_nombre = leer("Encriptados/prueba_1.txt")
    version_2 = ignorar_basura(texto)
    version_3, intermedio = BaseX_to_decimal(version_2) 
    conversiones = decimal_to_BI_OCT_HEX(intermedio, entrada)
    texto_completo = base_actual_a_ASCII(entrada, conversiones, ascii_dict)
    printeo(version_3, conversiones, texto_completo, entrada, archivo_nombre)
if __name__ == "__main__":
    main()