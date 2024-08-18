numbers = {1:"uno", 2:"dos", 3:"tres"} #En llaves
print (numbers)
print(numbers[1])
print(numbers[2])
print(numbers[3])

information = {"nombre": "Diego", 
               "apellidos": "Argote", 
               "edad": 27, 
               "estatura": 1.70,
               "esta feliz": True}
print(information)

del information ["apellidos"] #Elimina un elemento del diccionario
print(information)

claves = information.keys() #Devuelve todas las claves
print(claves)
print(type(claves))

valores = information.values() #Devuelve todos los valores
print(valores)

pairs = information.items() #Devuelve todas las claves y valores
print(pairs)

contacts = {"Diego": {"Apellido": "Argote", 
                      "Celular": 123456789,
                      "Altura": 1.70,
                      "Edad": 27,
                      "Signo zodiacal": "Escorpio",
                      "Serie favorita": "Samurai Jack",
                      "Cancion favorita": "Venecia sin ti - Charles Aznavour",
                      "Comida favorita": "Sushi",
                      "Lugar soñado vacaciones": "Florencia - Italia",
                      "Habilidad secreta": "manipulacion de la materia",
                      "Pasatiempo": "Entrenar",
                      "Heroe o persona que admiras": "Adria Sola Pastor",
                      "Libro que mas me ha impactado": "Hanitos atomicos",
                      "Cenar con alguien": "Leonardo Davinci",
                      "Superpoder": "Omnipresente",
                      "Que logro personal te enorgullese": "Ser mi mejor version cada dia"},
            
            "Dayra": {"Apellido": "Ortiz",
                      "Altura": 1.60,
                      "Edad": 55,}}

print(contacts)