# Recorrer una lista de números y mostrar los pares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
for i in numeros:
    if i % 2 == 0:
        print(i) 
        pares.append(i)
    
print(pares)