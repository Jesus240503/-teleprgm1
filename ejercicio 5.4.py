#Desarrolle una función en python que acepte una variable string como primer parámetro y la cantidad de caracteres de como segundo parámetro. La función debe retornar un nuevo string que consista en el string original y el número correcto de caracteres necesarios para que el string se salga centrado. No agregue caracteres al final del string

def centrado(a, b):
    espacio = ' '
    cuantos = int((b-len(a))/2)
    return f'{cuantos*espacio}{a}'

a = input('Introduzca una palabra: ')
b = int(input('Introduzca la cantidad de caracteres: '))

print(centrado(a, b))