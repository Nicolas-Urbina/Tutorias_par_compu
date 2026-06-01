def caja_negra (dato):
    largo = len(dato)
    dato1=""
    dato2=""
    operador=""
    i = 0
    t = 0
    while i<largo:
        if dato[i] != " " and t == 0:
            dato1 += dato[i]
        elif dato[i] == " ":
            t=1
        elif dato[i] == "+" or dato[i] == "-" or dato[i] == "/" or dato[i] == "*":
                operador = dato[i]
            
        elif dato[i] != " " and t == 1:
                dato2 += dato[i]
        
        i+=1


    dato1 = int(dato1)
    dato2 = int(dato2)
    print(dato1)
    print(dato2)
    if operador == "+":
        return dato1 + dato2
    if operador == "-":
        return dato1 - dato2
    if operador == "/":
        return dato1 / dato2
    if operador == "*":
        return dato1 * dato2
        
#programa 
dato = input('ingrese operacion y datos')
resultado = dato
#codigo

resultado = caja_negra(resultado)
print(resultado)