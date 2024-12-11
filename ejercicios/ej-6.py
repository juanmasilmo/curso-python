#Ordenar una lista manualmente (sin usar sort)

numeros = [11, 0, 2, 9, 0, 1, 8, 6, 10, 1]

for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        if numeros[i] > numeros[j]:
            numeros[i], numeros[j] = numeros[j], numeros[i]
            print(f"Intercambio: numeros[{i}]={numeros[i]} con numeros[{j}]={numeros[j]}")
    print(f"Después de la iteración {i}: {numeros}")

print("Lista final ordenada:", numeros)


   

        