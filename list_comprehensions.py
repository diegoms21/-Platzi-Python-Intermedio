def run():
    
#Guardamos los 100 primeros numeros la cuadrado en un arreglo
#Si el resto del numero es distinto de cero (osea que la division no es exacta y no es divisible entre 3), lo guardo en el arreglo
    # squares = []    
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         squares.append(i**2)
    

#Reemplazamos todo lo anterior en una sola linea    
    squares = [i**2 for i in range(1,101) if i % 3 != 0]
    #Para cada i en el rango de 1 a 101, voy a guardar esa i elevada al cuadrado solamente si el i modulo 3 es distinto de 0
    #Para cada i de los numeros del 1 al 100 vamos a guardar los numeros elevados al cuadrad solamente si no es divisible por 3
    print(squares)

def reto():
    reto = [i for i in range (1,100000) if (i % 4) == 0 and (i % 6) == 0 and (i % 9) == 0] #puede ser tambien if (i % 36) == 0
    print(reto)

if __name__ == '__main__':
    reto()

