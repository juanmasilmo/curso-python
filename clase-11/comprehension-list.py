#square = [x**3 for x in range(1,11)]
#print(f"los cuadrados son: {square}")

#lo que esta abajo es exactamente igual a lo que esta arriba

# Inicializar una lista vacía para almacenar los resultados
square = []

# Bucle for para calcular el cubo de cada número y agregarlo a la lista
for x in range(1, 11):
    valor = x**2
    print(f"Cuadrado  de {x}: {valor}")  # Imprimir cada valor calculado
    square.append(valor)

# Imprimir la lista final
print(f"Lista de Cuadrado: {square}")
