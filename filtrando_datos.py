DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    #lista que contendrá a todos los trabajadores de python del diccionario (el nombre de los trabajadores)
    #worker va a ser cada uno de los diccionarios internos (algo así como el "i" cuando recorremos un arreglo)
    #de worker quiero el contenido de la llave 'name'
    #de cada worker en DATA o cada trabajador en la lista DATA voy a guardar el contenido de la llave nombre solo si el contenido de lenguaje es python, osea solo si manejan python
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]

    for worker in all_platzi_workers:
        print(worker)
    #imprimo cada diccionario en la lista python_devs, recordar que colocar workers es como colocar "i"



    #Ahora se quiere filtrar a los mayores de 18 años
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    #ahora ya filtre a los mayores de edad en adults, pero si imprimimos adults, se verá que tenemos a todos los mayores filtrados como diccionarios y solo queremos los nombres, usaremos map
    adults = list(map(lambda worker: worker["name"], adults))

    #unimos un diccionario con otro nuevo (suma de diccionarios) con el "|" (funciona con python 3.9 en adelante)
    #lo que hace es que recibo de parametro un diccionario worker, entonces en cada worker le adicionaremos la clave "old" cone l valor que salga de evaluar la edad con 70 (True o False), el iterable que saremos será DATA
    #como usamos map, recorreremos toda la lista para modificarla y el resultado lo tendra old_people
    old_people = list(map(lambda worker: worker | {"old" : worker["age"] > 70}, DATA))

    for worker in adults:
        print(worker)

def reto():

    adults = [worker["name"] for worker in DATA if worker["age"] > 18] 
    for i in adults:
        print (i)   


    all_python_devs = list(filter(lambda worker: worker["language"] == "python",DATA))
    all_python_devs = list(map(lambda worker: worker["name"], all_python_devs))
    # for worker in all_python_devs:
    #     print(worker)

    all_platzi_workers = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_platzi_workers = list(map(lambda worker: worker["name"], all_platzi_workers))
    for worker in all_platzi_workers:
        print(worker)

if __name__ == '__main__':
    reto()
    



'''
{'Mac': '00:04:4b:e5:ad:66', 
'Colaboradores': 
    [{'Dni': '40821391', 'Temperatura': 36.39, 'Mascarilla': None, 'Acceso': True, 'TipoAcceso': 1, 'FechaHora': '2021-10-26 13:21:23', 'Foto': None, 'TicketPrinted': True, 'GenericQR': None, 'Servicio': 'ALMUERZO', 'IndMasivo': 'NO', 'NumServicios': 0, 'NumDietas': 0, 'Dieta': 'NO'}, {'Dni': '40821391', 'Temperatura': 36.47, 'Mascarilla': None, 'Acceso': True, 'TipoAcceso': 1, 'FechaHora': '2021-10-26 13:21:33', 'Foto': None, 'TicketPrinted': False, 'GenericQR': None, 'Servicio': 'ALMUERZO', 'IndMasivo': 'NO', 'NumServicios': 0, 'NumDietas': 0, 'Dieta': 'NO'}, 
    {'Dni': '40821391', 'Temperatura': 36.48, 'Mascarilla': None, 'Acceso': True, 'TipoAcceso': 1, 'FechaHora': '2021-10-26 13:21:44', 'Foto': None, 'TicketPrinted': False, 'GenericQR': None, 'Servicio': 'ALMUERZO', 'IndMasivo': 'NO', 'NumServicios': 0, 'NumDietas': 0, 'Dieta': 'NO'}, 
    {'Dni': '40821391', 'Temperatura': 36.41, 'Mascarilla': None, 'Acceso': True, 'TipoAcceso': 1, 'FechaHora': '2021-10-26 13:21:54', 'Foto': None, 'TicketPrinted': False, 'GenericQR': None, 'Servicio': 'ALMUERZO', 'IndMasivo': 'NO', 'NumServicios': 0, 'NumDietas': 0, 'Dieta': 'NO'}, {'Dni': '40821391', 'Temperatura': 36.53, 'Mascarilla': None, 'Acceso': True, 'TipoAcceso': 1, 'FechaHora': '2021-10-26 13:22:04', 'Foto': None, 'TicketPrinted': False, 'GenericQR': None, 'Servicio': 'ALMUERZO', 'IndMasivo': 'NO', 'NumServicios': 0, 'NumDietas': 0, 'Dieta': 'NO'}]}

'''