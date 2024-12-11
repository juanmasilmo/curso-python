from decimal import Decimal

x = 10
print(x)
print(type(x))

y = 5.123
print(y)
print(type(y))

'''z = 1.2e6
print(z)
print(type(z))

z = 1.2e-6
print(z)
print(type(z))'''

print("suma con redondeo: ", round(x + y))
print("resta con redondeo: ", round(x - y))
print("suma con Decimal es: ",y, " + ", x, " = ", Decimal(y) + Decimal(x))
print("suma con Decimal es convirtiendo y a cadena: ",y, " + ", x, " = ", Decimal(str(y)) + Decimal(x))#convierte a string y para garantizar que la suma sea precisa
print("Suma: ", y + y)

valor = 3.14159
print("Valor: {:.2f}".format(valor)) #:.2f indica que el número debe mostrarse con dos decimales