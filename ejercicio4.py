
#Ejercicio 4
def formato(numero):
    conversion= str(numero)
    conversion2=list(conversion)
    print (conversion2)
    lista_nueva=[]
    for indice,valor in enumerate(conversion2[::-1]):
        lista_nueva.append(valor)
        if indice%3==0 and indice>0:
            lista_nueva.pop(indice)
            lista_nueva.append(","+valor)
    conversion3="".join(lista_nueva)
    print(conversion3[::-1])



#Ejercicio 4.1
def formato(numero,tipo):
    conversion= str(numero)
    conversion2=list(conversion)
    print (conversion2)
    lista_nueva=[]
    for indice,valor in enumerate(conversion2[::-1]):
        lista_nueva.append(valor)
        if indice%3==0 and indice>0:
            lista_nueva.pop(indice)
            lista_nueva.append(tipo+valor)
    conversion3="".join(lista_nueva)
    print(conversion3[::-1])