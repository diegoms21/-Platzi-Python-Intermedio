def divisors(num):
    divisors = []
    for i in range (1 , num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    try:
        num = int(input("Ingresa un numero: "))
        print(divisors(num))
        print("El programa terminó")
    except ValueError:
        print("Debes ingresar un numero")

def reto():
    try:
        num = int(input("Ingresa un numero: "))
        if num < 0:
            raise ValueError('No puedes ingresar un numero negativo')       
        print(divisors(num))
        print("El programa terminó")
    except ValueError as ve:
        print(ve)

if __name__ == '__main__':
    reto()