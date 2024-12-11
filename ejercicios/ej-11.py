
n = 4
matriz = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n): 
    for j in range(n):
        if i == j:
            matriz[i][j] = 1
        else:
            matriz[i][j] = 0

for fila in matriz:
    print(fila)