filter = {"*": "01*","&": "01234567&","#": "0123456789#","!": "0123456789ABCDEF!"}
prefix_base = {"*": 2,"&": 8,"#": 10,"!": 16, 2: "*", 8: "&", 10: "#", 16: "!"}
hexadecimal_numbers_inverse = {"A": 10,"B": 11,"C": 12,"D": 13,"E": 14,"F": 15, 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

def Read_file(file_complete):
    file = open(file_complete,'r')
    text = file.read()
    file_name = file_complete.split("/")[-1]
    file.close()
    return text,file_name

def Filter(text,rules):
    clean_text = []
    copy = None
    group = []
    for i in text:
        if i in rules:
            copy = True
            actual = i
            group = []
            clean_text.append(group)
        if copy:
            if i in rules[actual]:
                group.append(i)
            else:
                copy = False
    return clean_text

def BaseX_to_decimal(clean):
    clean_decimal_filter = []
    decimal_numbers = []
    text_ascii = ""
    for i in clean:
        decimal_total = 0
        prefix = i[0]
        base = prefix_base[prefix]
        numbers = i[1:]
        exponent = len(numbers) -1
        for j in numbers:
            if j in hexadecimal_numbers_inverse:
                j = hexadecimal_numbers_inverse[j]
            j = int(j)
            decimal_total += ((base**exponent)* j)
            exponent -= 1

        if decimal_total >= 32 and decimal_total <= 126:
            clean_decimal_filter.append(i)
            text_ascii += chr(decimal_total)
            decimal_numbers.append(int(decimal_total))
    return clean_decimal_filter, decimal_numbers, text_ascii


def Decimal_to_BI_OCT_HEX(decimal_list,base):
    x_base_conversions = []
    for i in decimal_list: 
        group = "" 
        while i > 0: 
            remainder = i % base 
            i = i // base 
            if remainder in hexadecimal_numbers_inverse:
                remainder = hexadecimal_numbers_inverse[remainder] 
            group = str(remainder) + group 
        x_base_conversions.append(group)
    return x_base_conversions


def Show_results(decimal_clean,x_base_transformations,text_ascii,base,file_name):
    name_prefix = []
    for i in decimal_clean:
        prefijo = i[0]
        if prefijo == "*":
            name_prefix.append("Binario")
        elif prefijo == "&":
            name_prefix.append("Octal")
        elif prefijo == "#":
            name_prefix.append("Decimal")
        elif prefijo == "!":
            name_prefix.append("Hexadecimal")
        else:
            return
    print("\n", "[+] Procesando archivo: ", file_name, "...")
    print("[!] Filtrando ruido místico (valores fuera de rango ASCII)...\n "" ")
    print("LISTA DE VALORES EXTRAÍDOS (Base "+ str(base)+"): " + "\n--------------------------------------------------")
    print("[Proceso finalizado con éxito]")
    indice = 0 
    for i in range(len(decimal_clean)): 
        indice += 1
        print("Valor",str(indice)+ ":" ,x_base_transformations[i],"(Original:",name_prefix[i],"".join(decimal_clean[i]) + ")")
    print("--------------------------------------------------""\n""\nMENSAJE DECODIFICADO:")
    print(text_ascii,"\n" "\n[Proceso finalizado con éxito]")
    return

def main():
    print("             --- DECODIFICADOR DE NOTAS --- \n "" \n "" ") 
    base_input = int(input("Ingrese la base en la que desea visualizar los datos (2, 8, 10, 16): ")) 
    if base_input == 2 or base_input == 8 or base_input == 10 or base_input == 16: 
        pass
    else:
        print("Base incorrecta, vuelve a intentar")
        return
    
    text,file_name = Read_file("Encriptados/prueba_4.txt")
    clean_text = Filter(text,filter)
    clean_decimal_filter, decimal_numbers, text_ascii = BaseX_to_decimal(clean_text) 
    x_base_conversions = Decimal_to_BI_OCT_HEX(decimal_numbers, base_input)
    Show_results(clean_decimal_filter, x_base_conversions, text_ascii, base_input, file_name)
if __name__ == "__main__":
    main()