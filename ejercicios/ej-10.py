

#lista1 = [1, 2, 3, 4, 5]
#lista1 = [5, 4, 3, 2, 1]
lista1 = [3, 1, 4, 2]

fin = len(lista1)-1
asc = 0
desc = 0
for i in range(len(lista1) -1):
    print("Inicia el bucle")
    print (fin)
    print(lista1[i])
    if lista1[i] > lista1[i+1]:
        asc += 1 
    elif lista1[i] < lista1[i+1]:
        desc += 1
    print("termina el bucle")
print(asc)
print(desc)
print (range(len(lista1)))
if asc == fin:
     print(f"esta ordenado de manera descendente")
elif desc == fin:
    print(f"esta ordenado de manera ascendente")
else:
    print("esta desordenada")