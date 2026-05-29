# pedir al usuario que ingrese la catidad de datos que quieras del fibobacci 
# definir nuestras variables 
# Ciclo con la logica 
# imprimir durante el ciclo



# 0   1.   2.     3.     5.    8       13.      21.      34 


#cantidad_de_fibonacci = int(input("cunatos valores quieres"))


#p_inicial=1
#p_anterio=0
#p_siguiente=0

#print(p_anterio)

#i = 0
#while i<cantidad_de_fibonacci:
    #p_siguiente = p_inicial + p_anterio
    #print(p_siguiente)
    #p_anterio = p_inicial
    #p_inicial = p_siguiente
    #i+=1



#numeros primos 
# son numeros que se dividen entre si mismos y 1 



usuario = int(input("ingrese un numero")) 
i=2
bandera = True
while i < usuario:
    if usuario % i != 0 : 
        i+=1
    else: 
        bandera = False
        print(i)
        i = usuario
        
if (bandera):
    print("es primo")

else:
    print("no es primo") 
    


    

        





















    





