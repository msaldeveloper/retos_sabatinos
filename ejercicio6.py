
#ejercicio 6
#Crear una funcion que cree cajas basadas en un argumento

def caja(simbolo,tamaño=1):
    #contador=1
    print(simbolo*tamaño)
    for i in range(tamaño-2):
        #contador+=1
        if tamaño == 3:
            espacio=" "
            print(simbolo+espacio+simbolo)
        if tamaño > 3:
            espacio=" "*(tamaño-2)
            print(simbolo+espacio+simbolo)
    if tamaño > 1:
        print(simbolo*tamaño)
   