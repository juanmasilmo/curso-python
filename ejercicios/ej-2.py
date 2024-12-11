#cuantas vocales hay
texto = "ProgrAmaCiOn es DivERTIdo"
cont = 0
for i in texto:
    if i.lower() in "aeiou": #in es un operador que compara lo que esta en i si esta dentro(in) la cadena "aeiou", compara con cada vocal de la cadena
        print(i.lower())
        cont += 1

print("hay ", cont, " vocales")
