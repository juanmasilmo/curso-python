#square = [x**3 for x in range(1,11)]
#print(f"los cuadrados son: {square}")
#range es una funcion que recibe 3 parametros: range(start, stop, step(por defecto es uno))

#lo que esta abajo es exactamente igual a lo que esta arriba

# Inicializar una lista vacía para almacenar los resultados
square = []

# Bucle for para calcular el cubo de cada número y agregarlo a la lista
'''for x in range(1, 11):
    valor = x**2
    print(f"Cuadrado  de {x}: {valor}")  # Imprimir cada valor calculado
    square.append(valor)'''

# Imprimir la lista final
#print(f"Lista de Cuadrado: {square}")

celcius = [number for number in range(0, 150, 10)] 
print(celcius)

#temp se declara en el for porque en esa linea de codigo la prioridad es el for, primero el for, entonces al declarar temp en el for, despues cuando agarra valor de cada iteracion se hace la operacion del 9/5 * temp
farenheit = [(9/5 * temp ) + 32 for temp in celcius]
print(farenheit)

# aca sucede algo similar, primero se ejecuta el for, se declara x se itera con el range y despues hace el if solamente si cumple la condicion se guarda x en la lista
evens = [x for x in range(1,21) if x%2 == 0]
print(f"La cantidad de Numeros pares son: {evens}")

matrix = [[1,2,3], [4,5,6], [7,8,9]]
# aca se hace un for anidado, primero se itera sobre la matriz y despues sobre cada columna
transposed = [[row [i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)

#lo mismo de arriba pero de manera mas estructurada
'''transposed = []
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)'''