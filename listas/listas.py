to_do = ["alistar la pelicula",
         "freir las crispetas",
         "preparar pasabocas"]
print(to_do)

mi_dia = ["me levante a las 7am",
          "desayune",
          "hice ejercicio",
          "saque a mi perro",
          "lei un libro"]
print(mi_dia)

numbers = [1, 2, 3, 4, "cinco", 6, 7, 8, 9, 10]
print(numbers)
print (type(numbers))

mix = ["uno", 2, 3.14, True, [1, 2, 3]]
print(mix)
print (len(mix))

print("primer elemento:", mix[0])
print("segundo elemento:", mix[1])
print("tercer elemento:", mix[2])
print("cuarto elemento:", mix[3])
print("quinto elemento:", mix[4])
print("ultimoo elemento:", mix[-1])

print(mix[0:2])
print(mix[:2])
print(mix)
print(mix[2:])
print(mix[2:-2])
print(mix[2:len(mix)])

mix.append(False)
print(mix)

mix.append("Diego")
print(mix)

mix.insert(1,["a", "b", "c"])
print(mix)

print(mix.index(["a", "b", "c"]))

numbers = [1, 2, 100, 50.45, 3, 4, 5]
print("Mayor:", max(numbers))
print("Menor:", min(numbers))

del numbers[-1]
print(numbers)

del numbers [:2]
print(numbers)

del numbers
# print(numbers)


