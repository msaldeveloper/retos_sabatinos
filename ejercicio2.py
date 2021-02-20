#Ejercicio2
# Crear una funcion que reciba dos numeros como argumentos (numero, longitud), y 
#devuelva una lista con los multipos del numero dada la longitud

def multiplos(numero,longitud):
    if numero > 0 and longitud > 0 and isinstance(numero,int) and isinstance(longitud,int):
        lista_tablas=[numero*j for j in range(1,longitud+1)]
        return(lista_tablas)
    else:
        return("el dato ingresado no es correcto ingresa un numero entero")

    
    #print(f"{numero}X{j}={numero*j}") 