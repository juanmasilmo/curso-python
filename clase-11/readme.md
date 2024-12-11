transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]


Orden de Ejecución
range(len(matrix[0])):

Primero, Python evalúa la expresión range(len(matrix[0])). Esto determina el rango de valores para i, que son los índices de las columnas de la matriz.

len(matrix[0]): Se calcula la longitud de la primera fila de la matriz, que da el número de columnas.

range(...): Crea una secuencia de números desde 0 hasta len(matrix[0]) - 1.

for i in range(len(matrix[0])):

Python establece el bucle externo usando el rango calculado en el paso anterior.

En cada iteración del bucle externo, i toma un valor del rango generado.

[row[i] for row in matrix]:

Para cada valor de i, Python evalúa la lista de comprensión interna.

for row in matrix: Este bucle iterará sobre cada fila de la matriz.

row[i]: Para cada fila, toma el i-ésimo elemento (es decir, el elemento en la columna i).

Construcción de la lista interna:

La lista interna [row[i] for row in matrix] se completa para el valor actual de i, recopilando todos los elementos en la columna i.

Construcción de la lista externa:

La lista interna completa (una lista de elementos de la columna i) se añade a la lista transposed.

El bucle externo avanza al siguiente valor de i y repite el proceso.