import random
wu = 0
wc= 0

'''user1 = input("elije: 1: piedra, 2: papel o 3: tijera: ")
com = random.randint(1,3)
'''
while wu < 2 and wc < 2: 
    user1 = input("Elige: 1: piedra, 2: papel o 3: tijera: ") 
    user1 = int(user1)
    com = random.randint(1, 3) 
    print(f"COM eligió {com}") 
    print(f"USER eligió {user1}") 
    if user1 == 1 and com == 2: 
        print("Piedra pierde contra papel, perdiste") 
        wc += 1 
    elif user1 == 1 and com == 3: 
        print("Piedra gana tijera, Ganaste") 
        wu += 1 
    elif user1 == 2 and com == 1:
        print("Papel gana piedra, Ganaste") 
        wu += 1 
    elif user1 == 2 and com == 3: 
        print("Papel pierde con tijera, perdiste") 
        wc += 1 
    elif user1 == 3 and com == 1: 
        print("Tijera pierde contra piedra, perdiste") 
        wc += 1 
    elif user1 == 3 and com == 2: 
        print("Tijera corta papel, Ganaste!") 
        wu += 1 
    else: print("Empate")

print(f"Los puntos de User son: {wu} y los de Com son: {wc}")
        
    
