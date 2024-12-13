numbers = [1,2,3,4,5,6]

for i in numbers:
    print(f"el valor de i es: {i}")
    

for i in range(10):
    print(f"Este es un nuevo for y el valor de i es: {i}")
    
fruits = ["Manzana", "Pera", "Uva", "Naranja", "Sandia"]

for fruit in fruits:
    print(f"La fruta actual es {fruit}")
    if fruit == "Naranja":
        print(f"La fruta {fruit} encontrada")
        
x = 0

while x <= 5:
    print(f"Este es un while y el valor de x es: {x}")
    x += 1
    
y = 0
while y <= 5:
    print(f"Este es un while y el valor de y es: {y}")
    y += 1
    if y == 3: 
        print(f"Y alcanzo el valor necesario, se saldra del bucle y = {y}")
        break

numbers = [1,2,3,4,5,6]

for i in numbers:
    if i == 3:
        print(f"El valor de i es {i} se ejecuta el continue y no se imprimira el 3, continua el proceso pero salta cuando llega a un valor especifico")
        continue
    print(f"el valor de i es: {i}")