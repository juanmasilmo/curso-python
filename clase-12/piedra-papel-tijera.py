import random
wu = 0
wc= 0

'''user1 = input("elije: 1: piedra, 2: papel o 3: tijera: ")
com = random.randint(1,3)
'''
while wu <= 2 or wc <= 2:
    user1 = input("elije: 1: piedra, 2: papel o 3: tijera: ")
    com = random.randint(1,3)
    print(f"com eligio {com}") 
    print(f"USER eligio {user1}") 
    if user1 == "1" and com == "2":
        print("Piedra pierde contra papel, perdiste")
        wc += 1
    elif user1 == "1" and com == "3":
        print("Piedra gana tijera, Ganaste")
        wu += 1
    elif user1 == "2" and com == "1":
        print("Papel gana piedra, Ganaste")
        wu += 1
    elif user1 == "2" and com == "3":
        print("Papel pierde con tijera, perdiste")
        wc += 1
    elif user1 == "3" and com == "1":
        print("Tijera pierde contra piedra, perdiste")
        wc += 1
    elif user1 == "3" and com == "2":
        print("Tijera Corta papel, Ganaste!")
        wu += 1
    else:
        print("empate")
    
    
