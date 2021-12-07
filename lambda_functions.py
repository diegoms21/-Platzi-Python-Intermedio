#Las funciones lambda son funciones anonimas donde no se coloca el nomre de la funcion, en lugar de eso, a una variable le asignamos una función y le retornamos a esa variable el resultado de la funcion, el chiste esque las lambdas solo tienen una linea de código

def palindrome(string):
    return string == string[::-1]


palindrome_2 = lambda string: string == string[::-1]


if __name__ == '__main__':
    print(palindrome('ana'))
    print(palindrome_2('ana'))