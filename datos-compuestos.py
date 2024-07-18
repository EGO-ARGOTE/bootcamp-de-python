# El primer tipo de dato compuesto que veremos sera la lista

lista = ["Diego Argote", "Tecnotutoriales Jheyson Galvis", True, 1.70]
print(lista[1])
lista[3] = "Ego"
print(lista[3])

# La tupla es una lista que no se puede modificar

tupla = ("Diego Argote", "Tecnotutoriales Jheyson Galvis", True, 1.70)
print(tupla[1])
#tupla[1] = "Tips de Ego"
#print(tupla[1])

# Creado un conjunto o set
# Un conjunto no admite elementos duplicados

conjunto = {"Diego Argote", "Tecnotutoriales Jheyson Galvis", True, 1.70, 1.70}
print(conjunto)

# Creando un diccionario

diccionario = {
    "nombre": "Diego", 
    "apellidos": "Argote",
    "estatura": 1.70,
    "happy": True
    }

print(diccionario["happy"])
print(diccionario["nombre"])
print(diccionario["apellidos"])
print(diccionario["estatura"])
