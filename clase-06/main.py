from decimal import Decimal

name = input ("Decime tu nombre: ")
print("Hola! ", name)
print(type(name))
age = Decimal(input("Ahora tu edad: "))#cambiamos el tipo de dato, ahora solo puede recibir numerico
print("OH! tan joven! no pareces de ", age)
print(type(age))