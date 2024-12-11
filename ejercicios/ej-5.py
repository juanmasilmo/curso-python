#Encontrar el mayor número en una lista
'''def encontrar_mayor(lista):
    return max(lista)
#Encontrar el menor número en una lista
def encontrar_menor(lista):
    return min(lista)
#Encontrar el promedio de una lista
def encontrar_promedio(lista):
    return sum(lista) / len(lista)
'''

numeros = [150,34, 12, 56, 78, 23, 45, 100]
mayor = 0
for i in numeros:
    if i > mayor:
        mayor = i
        print(i)

print("el mayor numero es: ", mayor)

print("El mayor con funcion max es: ",max(numeros))