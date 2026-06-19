




m = []
i = 0 
columnas = int(input('dame las columnas'))
filas = int(input('dame las filas'))
while i < filas:
    j = 0
    l=[]
    while j < columnas:
        l.append(j)
        j += 1
    m.append(l)
    i+=1

for i in m:
    print(i)