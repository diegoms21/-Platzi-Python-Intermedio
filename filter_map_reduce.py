#el modulo reduce no viene directamente dentro del codigo functools
from functools import reduce

#ejemplos básicos de uso de filter, map y reduce

#filtro todos los pares y solo me quedo con impares
def filter_example():
    
    my_list = [1,4,5,6,8,9,12,13,15,16]
    #odd = [i for i in my_list if i % 2 != 0]
    odd = list(filter(lambda x: x%2 !=0, my_list))
    print(odd)

    #el lambda function recibe un numero y dice si es par o impar, nada mas
    #filter tiene 2 parametros, el primero es una funcion anonima (lambda) que devuelve true o false y el 2do es un iterable (cualquier elemento que se puede recorrer), en este caso es la lista donde aplicaremos los cambios
    #filter por si solo no nos devuelve la lista que queremos, porque devolverá un iterador, para armar la lista final usamos list

#elevo al cuadrado a todos los numeros de la lista
def map_examples():
    my_list = [1,4,5,6,8,9,12,13,15,16]
    #squares = [i**2 for i in my_list]
    squares = list(map(lambda x: x**2, my_list))
    print(squares)
    #se recorre cada elemento de la lista (my_list), lamda recibe el elemento x y retorna el x elevado al cuadrado y los va a guardar en una nueva lista llamada squares
    
def reduce_examples():
    my_list = [2,2,2,2,2]
    
    # all_multiplied = 1
    # for i in my_list:
    #     all_multiplied = all_multiplied * i
    all_multiplied = reduce(lambda a,b : a * b, my_list)

    print(all_multiplied)

    #ahora lambda recibe 2 valores: a y b.
    #a y b seran el primer y segundo valor de la iteracion del arreglo, en este caso serian 2 y 2, y cuando se multiplican, se guarda el 4 como nuevo valor del arreglo y luego ese pasa a ser el valor de a y b pasa a ser el valor que le toca, en este caso 2