#ejercicio5
lista=['apple','peach', 'apple','apple','conejo','gato','peach','conejo']
def pluralize(lista):
    nueva_lista=[]
    if not isinstance(lista,list):
        lista=list(lista)
    for i,j in enumerate(lista):
        if j not in nueva_lista:  
            nueva_lista.append(j)
            print(i,j) 
            
        else:
            pass
    return nueva_lista