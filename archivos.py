def read():
    numbers = []
    #con el ./ le indicamos que partimos desde la carpeta donde estamos actualmente, el encoding utf-8 es por si encontramos caracteres extraños en el idioma español que python no pueda interpretarlos (ñ o tildes)
    with open ("./archivos/numbers.txt","r", encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)



def write():
    names = ["diego", "juancho", "paola" , "pepito"]
    with open ("./archivos/names.txt","w",encoding="utf-8") as f:
        for name in names:
            f.write(name) #escribimos cada uno de los nombres
            f.write('\n') #escribimos un salto de linea

def run():
    read()
    write()

if __name__ == '__main__':
    run()