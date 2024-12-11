# Definir la matriz
matriz = [
    [7, 8, 9],
    [1, 2, 3],
    [4, 5, 6]
]

# Inicializar las sumas de las diagonales
suma_diagonal_principal = 0
suma_diagonal_secundaria = 0

# Obtener el tamaño de la matriz
n = len(matriz)

# Iterar sobre la matriz para sumar las diagonales
for i in range(n):
    # Sumar los elementos de la diagonal principal
    suma_diagonal_principal += matriz[i][i]
    # Sumar los elementos de la diagonal secundaria
    suma_diagonal_secundaria += matriz[i][n-i-1]

# Imprimir los resultados
print(f"Suma de la diagonal principal: {suma_diagonal_principal}")
print(f"Suma de la diagonal secundaria: {suma_diagonal_secundaria}")
