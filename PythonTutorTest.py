
texto = "*0001!321&112!41_LX#74&1PyLKvGr#74&1557&1417!41iWW+uNj#835#46"#Pequeña muestra
textv2 = []
copia = False 
temporal = ""
for letra in texto:
    if letra == "*" or letra == "#" or letra == "&" or letra == "!":
        if temporal != "":
            textv2.append(temporal)
        copia = True
        prefijo_buscar = letra
        temporal = ""
    if copia:
        if prefijo_buscar == "#" and letra not in ("0123456789#"):
            copia = False
        elif prefijo_buscar == "*" and letra not in ("01*"):
            copia = False
        elif prefijo_buscar == "&" and letra not in ("01234567&"):
            copia = False
        elif prefijo_buscar == "!" and letra not in ("0123456789ABCDEF!"):
            copia = False
    if copia:
        temporal += letra
    else:
        if temporal != "": 
            textv2.append(temporal)
            temporal = ""
textv2.append(temporal)

print(textv2)