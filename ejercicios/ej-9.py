# Convertir una matriz en una lista plana (flatten):

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
array = []
# Salida esperada: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"la matriz es de: {range(len(matriz))}")
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        array.append(matriz[i][j])

print(f"El arary quedo asi: {array}")