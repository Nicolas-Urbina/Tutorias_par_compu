def transformar_a_complemento_a_2(numero, tamaño):
    numero_binario = [0] * tamaño 
    #[0,0,0,0,0,0,0,0]
    numero_entero_aux = numero
    numero_bin_aux = [0] * tamaño
    numero_bin_aux[0] = 1
    i = tamaño - 1 
    while (i >= 0):
        numero_binario[i] = numero % 2
        numero = numero // 2
        i -=1
    
    i = 0 
    while ( i < tamaño):
        if (numero_binario[i] == 0):
            numero_binario[i] = 1
        else :
            numero_binario[i] = 0
    
    return sumar(numero_binario,numero_bin_aux)

def sumar(numero_binario,numero_bin_aux):

    return 


bandera = True
while (bandera):
    bandera = False
