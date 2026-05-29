def total_contenedores_(volumen):
    volumen = volumen * 1024
    t_contendor1 = 11
    t_contendor2 = 7
    t_contendor3 = 3

    if volumen % t_contendor1 == 0:
        return "cantidad de contenedores de espacio 11 usados" , volumen // t_contendor1
    else:
        cantidad_c1 = volumen // t_contendor1
        resto = volumen % t_contendor1
        cantidad_c2 = resto // t_contendor2
        resto = resto % t_contendor2
        cantidad_c3 = resto // t_contendor3
        resto = resto % t_contendor3
        return "cantidad de contenedores de tamañano 11:" , cantidad_c1 , " cantidad de contenedores usados tamaño 7:" , cantidad_c2 , " cantidad de contenedores usados tamaño 3:" , cantidad_c3 , " sobrantes:" , resto






def total_contenedores(t_contenedor1,t_contenedor2,t_contenedor3,volumen):
    volumen = volumen * 1024

    if volumen % t_contenedor1 == 0:
        cantidad = volumen/t_contenedor1
        print(cantidad)
        return "cantidad de contenedores de espacio 11 usados" , cantidad
    else:
        cantidad_c1 = volumen // t_contenedor1
        resto = volumen % t_contenedor1
        cantidad_c2 = resto // t_contenedor2
        resto = resto % t_contenedor2
        cantidad_c3 = resto // t_contenedor3
        resto = resto % t_contenedor3
        return "cantidad de contenedores de tamañano" ,t_contenedor1,":", cantidad_c1 , " cantidad de contenedores usados tamaño" ,t_contenedor2,":" , cantidad_c2 , " cantidad de contenedores usados tamaño" ,t_contenedor1,":", cantidad_c3 , " sobrantes:" , resto




print(total_contenedores(10,8,2,1))
print(total_contenedores_(3))
