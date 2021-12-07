def divisors(num):
    divisors = []
    for i in range (1 , num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    
    num = input("Ingresa un numero: ")
    assert num.isnumeric(), "Debes ingresar un numero"
    print(divisors(int(num)))
    print("El programa terminó")
 
#isnumeric es un metodo propio de la cadena de caracteres o string, devuelve True si el string corresponde a una especie de numeros o False caso contrario
#para que funcione debe eliminarse el casteo con el int()

def reto():
    num = input("Ingresa un numero: ")
    assert num.isnumeric() and int(num) > 0, "Debes ingresar solo numeros positivos"
    print(divisors(int(num)))
    print("El programa terminó")

if __name__ == '__main__':
    reto()