x= 5
y = 20

if x > 10 and y > 15:
    print(f"X: {x} es mayor que 10 y Y: {y} es mayor que 15")
    
if x > 10 or y > 15:
    print(f"X: {x} es mayor que 10 o Y: {y}")
    
if not x > 20:
    print(f"X: {x} no es mayor que 20")

is_member = False
age = 19

if is_member:
    if age < 18:
        print("Eres menor que 18 años pero eres miembro")
    else:
        print("Eres mayor que 18 años y eres miembro")
else:
    print("No eres miembro")