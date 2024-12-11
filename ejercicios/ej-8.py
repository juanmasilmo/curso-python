

lista = [1, 2, 3, 4, 5]
rango = len(lista) -1
intercambio = 0
for i in range(len(lista) // 2):
    intercambio = lista[i]
    lista[i] = lista[rango]
    lista[rango] = intercambio
    rango -= 1
print(f"el array invertido quedo asi: {lista}")

''' con while
lista = [1, 2, 3, 4, 5]
inicio = 0
fin = len(lista) - 1

while inicio < fin:
    # Intercambiar elementos
    lista[inicio], lista[fin] = lista[fin], lista[inicio]
    
    # Mover los índices hacia el centro
    inicio += 1
    fin -= 1

print(f"El array invertido quedó así: {lista}")
'''