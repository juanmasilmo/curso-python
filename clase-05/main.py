from decimal import Decimal

a = Decimal('10') # Usamos Decimal('10') o Decimal('3') porque Decimal convierte la cadena a un número decimal adecuado, lo que nos permite realizar operaciones matemáticas precisas sin problemas de redondeo o precisión.

b = Decimal('3')

res = 0
print(type(a))
print(type(b))
res = a / b
res = res.quantize(Decimal('0.01'))
print(f"Resultado : {res}")

print("La Suma es: ", a + b)
print("La Resta es: ", a - b)
print("La Multiplicacion es: ", a * b)
print("La potenciacion es: ", a ** b)
print("La Division es: ", a / b)
print("La parte entera de la Division es: ", a // b)
print("La Resto es: ", a % b)