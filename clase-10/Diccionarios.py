#diccionario: concepto: esta formado por una key,en number la key es 1, 2 o 3, es decir el primer dato, puede ser n:"algo" donde n es la key y "algo" es el valor

numbers = {1: "uno", 2:"dos", 3:"tres"}
print(numbers)
print(numbers[1]) # prints "uno"

information = { "name" : "juanma", 
               "lastname" : "Silmo", 
               "age" : 39,
               "city" : "Posadas"
               }

print(information)
print(information["name"]) # prints "juanma"
print(information["lastname"]) # prints "Silmo"

del information["age"]
print(information) # prints {"name": "juanma", "lastname": "Silmo",

claves = information.keys()
print(claves) # prints dict_keys(['name', 'lastname', 'city'])
print(type(claves))

values = information.values()
print(values) # prints dict_values(['juanma', 'Silmo', 'Posadas'])
print(type(values))

pairs = information.items()
print(pairs)

agenda = {  
    "juanma": { 
               "lastname" : "Silmo", 
               "age" : 39,
               "city" : "Posadas"
               },
    
    "Fulano" : {
        "lastname" : "mengano",
        "age" : 30,
        "city" : "Rosario"
    }
}

print(agenda)
print(agenda["juanma"])