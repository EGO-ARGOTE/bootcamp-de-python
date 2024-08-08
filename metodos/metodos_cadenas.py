cadena1 = "Hola,soy,Ego"
cadena2 = "Gracias por aprender Python"
# print(dir(cadena1))

resultado = cadena1.upper() #todo a mayuscula
print(resultado)

resultado = cadena1.lower() #todo a minuscula
print(resultado)

primera_letra_mayus = cadena1.capitalize() #primera letra en mayuscula
print(primera_letra_mayus)

busqueada_find = cadena1.find("soy") #busca la palabra
print(busqueada_find)

busqueada_index = cadena1.find("z") #busca la letra
print(busqueada_index)

busqueada_index = cadena1.index("a") #si la letra no existe da error
print(busqueada_index)

es_numerico = cadena1.isnumeric() #verifica si es numerico
print(es_numerico)

es_alfanumerico = cadena1.isalpha() #verifica si es alfanumerico
print(es_alfanumerico)

contar_coincidencias = cadena1.count("a") #contar coincidencias
print(contar_coincidencias)

contar_caracteres = len(cadena1) #contar caracteres
print(contar_caracteres)

empieza_con = cadena1.startswith("Hola") #empieza con
print(empieza_con)

termina_con = cadena1.endswith("*") #termina con
print(termina_con)

cadena_nueva = cadena1.replace("soy", "yo me llamo") #reemplazar
print(cadena_nueva)

cadena_separada = cadena1.split(",") #separar
print(cadena_separada)
print(type(cadena_separada))
print(cadena_separada[0])