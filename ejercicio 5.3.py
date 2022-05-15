#Dado una lista de enteros, defina una función en python que devuelva la suma de solo los valores impares de dicha lista

lista= [1,2,3,4,5,6,7,8,9]

def sumar_impares(lista):
    if len (lista) == 0:
        return 0
    elif lista[0] % 2 !=0:
        return lista[0] + sumar_impares(lista[1:])
    else:
        return sumar_impares(lista[1:])
print (sumar_impares(lista))