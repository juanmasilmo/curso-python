#listas

to_do = [
        "ir al telo",
        "almorzar",
        "ir a la playa",
        "ir a la tienda",
        "ir a la biblioteca",
        ]

misture = [1,2,123456789,4,"cinco", 3.14,"juanma", to_do]
print(misture)
print(type(misture))

print(len(misture))

print("octavo elemento de la lista: ", misture[7][3])# asi se pone para imprimir lo que esta en la lista dentro de la lista en la posicion 7 hay una lista y de esa lista buscamos la posicion 3 y mostramos que hay

print("octavo elemento de la lista: ", misture[7])
print("cuarto elemento de la lista: ", misture[3])
print("ultimo elemento de la lista: ", misture[-1])
print("Seleccionando desde donde  hasta donde mostrar: ", misture[0:3])

cadena = "hola mundo"
print(cadena[0])#imprime la primera letra de la cadena
print(cadena[:4]) #se muestra desde el principio hasta 4
print(cadena[5:]) #se muestra desde la posicion 5 hasta el final
misture.append(False)
print(misture) #agrega un elemento al final de la lista

to_do.insert(0, ["posicion 0", "posicion 1"])
print(to_do) #inserta un elemento en la posicion 0 de la lista
numbers = [1,2,50,30,80,100,1568,1234,0]
#ordenar la lista de menor a mayor
numbers.sort()
print(numbers)
print("El mayor es: ",max(numbers))
print("El menor es: ",min(numbers))
numbers.reverse()
print(numbers) #invierte el orden de la lista
print("La suma de los elementos es de: ", sum(numbers))
print("El promedio es: ",sum(numbers)/len(numbers)) #calcula el promedio


