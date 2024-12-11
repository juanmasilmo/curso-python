#tuplas
'''matrix = [[1,2,3],
        [4,5,6],
        [7,8,9]]

print(matrix)
print(matrix[2][2])'''

matrix2 = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
]

'''print(matrix2)
print(matrix2[2][1][1])
#matrix2.sort(reverse=True)
print(matrix2)'''

'''print("aca deberiaimprimir 9 10 11 12: ", matrix2[2])
matrix2[2][0].sort(reverse=True)# ordena el primer array del array 2
matrix2[2][1].sort(reverse=True)# ordena el segundo array array del array 2
matrix2[2].sort(reverse=True) # ordena el array 2 entero
print("aca se deberia imprimir 12,11,10,9: ",matrix2[2]) # aca deberia imprimir [12, 11, 10, 9]
matrix2[0][0].sort(reverse=True)
matrix2[0][1].sort(reverse=True)
matrix2[0].sort(reverse=True) #deberia estar ordenado de mayor a menor todo el array 0
print(matrix2[0])

matrix2[1][0].sort(reverse=True)
matrix2[1][1].sort(reverse=True)
matrix2[1].sort(reverse=True) #deberia estar ordenado de mayor a menor todo el array 1
print(matrix2[1])'''

# esto es lo mismo que arriba, que se hace aca? en el for i, i va a recorrer cada elemento de la lista principal matrix2 por eso es "i in matrix2" cada elemento lo toma como array digamos elemento bidimensional nomas [[1, 2], [3, 4]] x ej despues j recorre individualmete [1, 2] y los ordena
for i in matrix2:
    print("esto recorre i: ", i)
    for j in i:
        print("esto recorre j: ",j)
        j.sort(reverse=True)
        print("esto ordeno j en la iteracion: ",j)
    i.sort(reverse=True)
    print("Esto ordeno i despues de que j ordenara los arrays individualmente: ",i)

matrix2.sort(reverse=True)
print(matrix2)