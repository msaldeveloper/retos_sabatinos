# retos_sabatinos

# Ejercicio 1

Crear una funcion que reciba un numero como argumento y devuelva el largo de este numero

**Ejemplos**
numero_length(10)-->2
numero_length(100)-->3
***restricciones**
- El numero no puede ser negativo
- El numero que se manda a la funcion tiene que ser de tipo INT
- no se puede usar el metodo length



# Ejercicio 2
Crear una funcion que reciba dos numeros como argumentos (numero, longitud), y 
devuelva una lista con los multipos del numero dada la longitud

**Ejemplos**
list_of_multiles(7,5)-->[7,14,21,28,35]
**Notas**
Vean que la lista contiene el numero que le pasan como argumento
**Restricciones**
- Los argumentos no pueden ser negativos
- Los argumentos deben ser enteros

# Ejercicio 3
Crear una funcion que devuelva el factorial de un numero
**Ejemplos**
factorial(3)-->6(321)
- investigar que demonios es la recursividad

# Ejercicio 4
Crear una funcion que formatee numeros ￼

**Ejemplos**

format_numer(1000) -> '1,000'

format_numer(43214124) -> '43,214,124'

**Restricciones**

El argumento no puede ser negativo
El argumento deben ser entero
### **Ejercicio 4.1**
Agregar el separador que el usuario indique
**Ejemplo**

format_numer(1000,'#') -> '1#000'

format_numer(43214124) -> '43#214#124'


# Ejercicio 5
Crear una funcion que pluralice si un elemento se repite en una lista dada como argumento
- El resultado tiene que ser un iterable (tuple, lista o set)

**Ejemplos**

`pluralize(['apple','peach', 'apple']) -> ['apples','peach'] || ('apples', 'peach') || {'apples', 'peach'}`  

`pluralize(['cat', 'dog', 'cat', 'cat', 'dog', 'rabbit']) -> ['cats','dogs', 'rabbit'] || ('cats', 'dogs', 'rabbit') || {'cats', 'dogs', 'rabbit'}`

**Restricciones**
- El argumento tiene que ser una lista `[]`
￼
￼
# Ejercicio 6

Crear una funcion que cree cajas basadas en un argumento

**Ejemplos**

```python
￼make_box(1) 
￼[
￼    "#"
￼]
￼
￼make_box(2) 
￼[
￼    "##",
￼    "##",
￼]
￼
￼make_box(3) 
￼[
￼    "###"
￼    "# #",
￼    "###",
￼]
￼
￼make_box(4) 
￼[
￼    "####",
￼    "#  #",
￼    "#  #",
￼    "####",
￼]