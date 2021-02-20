"""
funcion que al ingresar un numero entero te devuelve 
la longitud de ese numero 
"""
def contador(numero):
    if type(numero) != int or numero<0:
        return ("numero incorrecto porfavor ingresa un entero")
    else:
        cambio=str(numero)
        contador=0
        for i in cambio:
            #print (i)
            contador+=1
        return (f"la longitud de tu numero es {contador}")

