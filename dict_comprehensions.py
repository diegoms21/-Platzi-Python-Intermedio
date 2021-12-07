import math 
def run():
    
    # my_dict = {}
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         my_dict[i] = i**3

#Para cada i en el rango de 1 a 101, vamosa guardar a i como llave y a i al cubo como valor solamente si i modulo 3 es distinto de 0
#Para cada numero de 1 a 100 vamos a guardar ese numero como llave y como valor si este numero no es divisible entre 3
    my_dict = {i : i**3 for i in range(1,101) if f % 3 != 0}

    print(my_dict)

def reto():
    #reto = {i : round(i**0.5,2) for i in range(1,1000)}
    reto = {i : round(math.sqrt(i),2) for i in range(1,1000)}
    print (reto)

if __name__ == '__main__':
    reto()