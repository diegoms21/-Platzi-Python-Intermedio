def run():
    my_list = [1 , "Hello", True, 4.5]
    my_dict = {"firstname" : "diego", "lastname" : "tarazona"}

    #Lista de diccionarios (cada valor de la lista es un diccionario)
    super_list = [
        {"firstname" : "diego", "lastname" : "tarazona"},
        {"firstname" : "pepe", "lastname" : "pancho"},
        {"firstname" : "pepito", "lastname" : "pepitito"},
        {"firstname" : "juancho", "lastname" : "papijuancho"}
    ]
    
    #Diccionario de listas (cada valor del diccionario es una lista)
    super_dict = {
        "natural_nums" : [0,1,2,3,4,5],
        "integer_nums" : [-1,-2,-3,-4,-5,0],
        "float_nums" : [1.1 , 2.2 , 3.3 , 4.4]
    }

    #el metodo item nos permite recorrer las llaves y valores de un diccionario en un mismo ciclo
    for key, value in super_dict.items():
        print(key, "-" , value)

if __name__ == '__main__':
    run()