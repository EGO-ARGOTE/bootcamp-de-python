# Ejemplo de como funcionan los iteradoras
# Lista de numeros
my_list = [1, 2, 3, 4]

# Obtener iterador de la lista
# Un iterador es un objeto que permite recorrer una secuencia de datos
my_iter = iter(my_list)

#Usar iteradorpara acceder a elementos de la lista
# La funcion next() permite acceder al siguiente elemento de la lista
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# iterar cadenas de texto usando un iterador
# crear cadena de texto
text = "Hola mundo"

#crear iterador para la cadena
# Un iterador es un objeto que permite recorrer una secuencia de datos
iter_text = iter(text)

#iterar sbre cada caracter de la cadena utilizando un bucle for
for char in iter_text:
  print(char)

# crear un iterador que genere numeros impares desde el 1 hasta el limite
# range (1, limit+1, 2) genera impares desde 1 hasta el limite
odd_iter = iter(range(1, 10, 2))

# usar iterador para recorrer y mostrar los impares
for num in odd_iter:
  print(num)
  
# definir una funcion generadora
def my_gen():
  yield 1  # la palabra clave yield permite retornar un valor
  yield 2
  yield 3
    
# usar un buvle for para iterar sobre los valores generados
for value in my_gen():
  print(value)
  
# fibonacci
# la serie de fibonaccia hace referencia a que el siguiente numero es la suma de los dos anteriores
def fibonacci(limit): # inicializa los dos primeros valores
  a, b = 0, 1
  while a < limit: # mientras a sea menor que el limite
    yield a
    a, b = b, a + b

for num in fibonacci(10):
  print(num)