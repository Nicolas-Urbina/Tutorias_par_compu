def convertir_numero_base_10_a_binario_complemento_2(numero, configuracion):
    numero_bin = [0] * configuracion
    numero_bin_aux = [0] * configuracion
    numero_bin_aux[0] = 1
    i = configuracion -1
    numero_entero_aux = numero 
    while (i > 0):
        numero_bin[i] = numero % 2
        numero = numero // 2
        i -= 1
    i=0
    while (i < configuracion):
        if (numero_bin[i] == 0):
            numero_bin_aux[i] = 1
        else:
            numero_bin_aux[i] = 0
        i+=1
    return sumar(numero_bin_aux,numero_bin_aux,configuracion)

def convertir_numero_a_base_10(numero):
    numero_base_10 = 0
    for i in range(len(numero)):
        numero_base_10 += numero[i] * (2 ** i)
    return numero_base_10

def verificar_overflow_entero(numero):
    return True

def sumar (numero_b2_1,numero_b2_2,configuracion):
    acarreo = 0
    resultado = [0] * configuracion
    i = 0 
    while (i < len (numero_b2_1)):
        if (numero_b2_1[i] + numero_b2_2[i] + acarreo == 0):
            resultado.append(0)
            acarreo = 0
        elif (numero_b2_1[i] + numero_b2_2[i] == 1 + acarreo == 1):
            resultado.append(1)
            acarreo = 0
        
        elif (numero_b2_1[i] + numero_b2_2[i] == 1 + acarreo == 2):
            resultado.append(0)
            acarreo = 1
        
        elif (numero_b2_1[i] + numero_b2_2[i] == 1 + acarreo == 3):
            resultado.append(1)
            acarreo = 1
        i+=1
    return resultado

def multiplicar (numero_b2_1,numero_b2_2,configuracion):
    i = 1
    valor_entero = convertir_numero_a_base_10(numero_b2_2)
    resultado = [configuracion]
    while (i <= valor_entero):
        resultado = sumar(numero_b2_1,resultado,configuracion)
        i+=1
    return resultado

def restar (numero_b2_1,numero_b2_2,configuracion):
    resultado = [configuracion]
    i = 0
    while (i < len(numero_b2_1)):
        if (numero_b2_1[i] == numero_b2_2[i]):
            resultado.append(0)
        elif (numero_b2_1[i] == 1 and numero_b2_2[i] == 0):
            resultado.append(1)
        elif (numero_b2_1[i] == 0 and numero_b2_2[i] == 1):
            resultado.append(1)
            j = i + 1
            while (j < len(numero_b2_1) and numero_b2_1[j] == 0):
                numero_b2_1[j] = 1
                j+=1
            if (j < len(numero_b2_1)):
                numero_b2_1[j] = 0
        i+=1
    return resultado

def division (numero_b2_1,numero_b2_2,configuracion):
    resultado = [configuracion]
    i = 1
    valor_entero = convertir_numero_a_base_10(numero_b2_2)
    while (i <= valor_entero):
        resultado = restar(numero_b2_1,resultado,configuracion)
        i+=1
    
    return resultado


configuracion = int (input('Configurando la máquina Ingrese el tamaño de palabra con el que desea trabajar, en bits: 8. '))
print('........')
print('Ha configurado exitosamente su máquina.')

bandera = True
numero_1 = [0] * configuracion
numero_2 = [configuracion] * configuracion
resultado = 0

while bandera:
    print('[1]: suma')
    print('[2]: resta')
    print('[3]: multiplicación')
    print('[4]: división')
    print('[0]: apagar')
    
    entrada = input()
    if (entrada != 0):
        i=0
        opcion = int(entrada[i])
        i+=2
        primer_numero = int(entrada[i])
        i+=2
        segundo_numero = int(entrada[i])
        if (verificar_overflow_entero(primer_numero) and verificar_overflow_entero(segundo_numero)):
            numero_1 = convertir_numero_base_10_a_binario_complemento_2(primer_numero,configuracion)
            numero_2 = convertir_numero_base_10_a_binario_complemento_2(segundo_numero,configuracion)

            if (opcion == 1):
                resultado = convertir_numero_a_base_10(sumar(numero_1,numero_2,configuracion))
                print(primer_numero, ' + ', segundo_numero, ' = ', resultado  )

            elif (opcion == 2):
                resultado = convertir_numero_a_base_10(restar(numero_1,numero_2,configuracion))
                print(primer_numero, ' - ', segundo_numero, ' = ', resultado  )

            elif (opcion == 3):
                resultado = convertir_numero_a_base_10(multiplicar(numero_1,numero_2,configuracion))
                print(primer_numero, ' * ', segundo_numero, ' = ', resultado  )

            elif (opcion == 4):
                resultado = convertir_numero_a_base_10(division(numero_1,numero_2,configuracion))
                print(primer_numero, ' / ', segundo_numero, ' = ', resultado  )
        else: 
            print ('ERROR de overflow en los valores ingresados')
    else: 
        bandera = False
        






    



