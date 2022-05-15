#Ejercicio 5.1 Defina una funcion en python que acepte la radio y devuelva el valor del area de un circulo de esas dimensiones

from math import pi
radio = float(input("Ingrese el radio del círculo:\n"))
area = round((pi * radio ** 2), 3)
print(f"El área del círculo es: {area}")