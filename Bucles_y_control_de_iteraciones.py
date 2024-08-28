numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
  print("Aqui i es igual a:", i + 1) # la variable i toma los valores de 1 a 6

for i in range(3, 10): # la variable i toma los valores de 3 a 9
  print(i)
  
fruits = ["apple", "banana", "cherry", "orange", "kiwi"]
for fruit in fruits:
  print(fruit)
  if fruit == "kiwi": # si la variable fruit es igual a kiwi
    print ("I found it!") # imprime "I found it!"
    
x = 0
while x < 5: # la variable x toma los valores de 0 a 5
  if x == 3: # si la variable x es igual a 3
    break # rompe el bucle
  print(x)
  x += 1
  
numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
  if i == 3:
    break
  print ("Aqui i es igual a:", i + 1)