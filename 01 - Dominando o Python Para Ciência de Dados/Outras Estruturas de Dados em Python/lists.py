frutas = ["banana", "maçã", "uva"]

letras = list("Gabriel Leone")

numeros = list(range(10))

carro = ["Fusca", 15000, "Volkswagen", True]

print(frutas)
print(letras)
print(numeros)
print(carro)

print(frutas[0])

matriz = [
  [1, 2, 3], 
  [4, 5, 6], 
  [7, 8, 9]]
print(matriz)
print(matriz[0])
print(matriz[0][0])

motos = ["Honda", "Yamaha", "Suzuki"]

for indice, carro in enumerate(motos):
  print(indice, carro)

numbers = [1, 30, 21, 2, 9, 65, 34]
# pares = []

# for number in numbers:
#   if number % 2 == 0:
#     pares.append(number)

# print(pares)

pares = [number for number in numbers if number % 2 == 0]

quadrado = [number ** 2 for number in numbers]

print(pares)
print(quadrado)

### MÉTODOS

lista = []

lista.append(1)
lista.append("Gabriel")
lista.append(True)
lista.append(1.5)
lista.append([1, 2, 3])
lista.append({"nome": "Gabriel"})

print(lista)

lista.insert(2, "Leone")
print(lista)

l2 = lista.copy()

lista.clear()

print(l2.count('Gabriel'))

lista.extend(l2)

print(lista)

print(lista.index('Leone'))

print(lista.pop(2))

print(lista.pop())

print(lista)

lista.remove('Gabriel')

print(lista)

lista.reverse()

# lista.sort() só funciona para listas com o mesmo tipo de dado

print(lista)

print(len(lista))

