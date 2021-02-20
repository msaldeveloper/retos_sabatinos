#Ejercicio 3
#Crear una funcion que devuelva el factorial de un numero

def factorial(numero):
    fac = 1
    for i in range(1,numero+1):
        fac=fac*i
    return fac
    