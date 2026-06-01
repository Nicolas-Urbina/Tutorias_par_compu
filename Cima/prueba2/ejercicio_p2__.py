dato1 = input('ingrese datos')
dato2 = input('ingrese datos')

bandera = 0

#para el primer dato
i = 0
while (i < len(dato1)):
    if dato1[i] != '.' :
        i+=1
    else :
        i = len(dato1) + 1

if i == len(dato1):
    dato1 = int(dato1)
else:
    if i == len(dato1 ) + 1:
        dato1 = float(dato1)
        bandera = 1

#para el segundo 

i = 0
while (i < len(dato2)):
    if dato2[i] != '.' :
        i+=1
    else :
        i = len(dato2) + 1

if i == len(dato2):
    dato2 = int(dato2)
else:
    if i == len(dato2 ) + 1:
        dato2 = float(dato2)
        bandera = 1





if bandera == 1:
    resultado = float(dato1) + float(dato2)
else :
    resultado = dato1 + dato2 

print(resultado)
