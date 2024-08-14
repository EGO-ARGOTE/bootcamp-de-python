lista = list ([1996, 9, 11, True]) #Elimine hola y Ego

# Nos permite saber la longitud de la lista (cantidad de caracteres)
cadena = "Hola, soy, Ego"
resultado = len(lista)

#Agregando un elemnto a la lista
lista.append(4) #agregando un elemento

#Agregando un elemento en una posicion especifica
lista.insert(2, False) #agregando un elemento false

#Agregando varios elementos a la lista
lista.extend(["2024"]) #quite egolutions

#Eliminando un elemento de la lista
print(len(lista))
lista.pop(0)
print(len(lista))
lista.pop(-1) #Elimina el ultimo elemento de la lista

#Eliminando un elemento de la lista por su valor
# lista.remove("Egolutions")

#Ordena los elementos de la lista mientras a lista tenga numeros y booleanos
lista.sort()
lista.sort(reverse=True)

#Verifica si un elemento se encuentra en la lista
elemento_encontrado = lista.index(11)

print(elemento_encontrado)
