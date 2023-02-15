"""1. Hacer una lista que contenga números junto con algunos strings.
2. Hacer una función que devuelva el tipo de dato (type) de los diferentes elementos de la lista"""

lst = [10, 20, "rana", "vejiga",30,1]
print (lst[0])
print (lst[1])
print (lst[3])


#Para obtener el tipo de cada elemento en una lista en Python, 
# puedes recorrer la lista usando un bucle for y usar la función type() para obtener el tipo de cada elemento.
# Esta función crea una lista vacía llamada tipos, luego recorre la lista de entrada y para cada elemento, 
# obtiene su tipo utilizando type(elemento) y lo agrega a la lista tipos. 
# Finalmente, la función devuelve la lista de tipos resultante.
def tipo_elementos (lista):                          #
    lst_elementos = []
    for elemento in lista:
        lst_elementos.append(type(elemento))
    return lst_elementos

lst_elementos = [10, 20, "rana", "vejiga",30,1]
tipo_elementos (lst_elementos)
print (type(tipo_elementos))
print (type(lst_elementos))
print (tipo_elementos(lst_elementos))
