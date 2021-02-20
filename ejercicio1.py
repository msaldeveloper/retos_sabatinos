def contador(numero):
    if type(numero) != int:
        return("ingresa un numero entero no una cadena de texto")
    elif numero>0: 
        cambio=str(numero)
        contador=0
        for i in cambio:
            #print (i)
            contador+=1
        return (f"la longitud de tu numero es \n{contador}")
    
    else:
        return ("numero invalido ingresa un numero entero")