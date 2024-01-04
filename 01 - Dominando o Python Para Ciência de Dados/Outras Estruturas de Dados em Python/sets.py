numeros = set([1,2,3,1,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,1])

fruta = set("abacaxi")

carros = set(["palio", "gol", "fusca", "palio", "gol", "fusca"])

print(numeros)
print(fruta)
print(carros)

# Para acessar os valores, precisa transformar o set em uma lista

print(list(numeros)[0:5])

### METODOS

conjunto_a = {1, 2}
conjunto_b = {2, 3}

print(conjunto_a.union(conjunto_b))
print(conjunto_a.intersection(conjunto_b))
print(conjunto_a.difference(conjunto_b))
print(conjunto_a.symmetric_difference(conjunto_b))

conjunto_c = {1, 2, 3, 4, 5}
print(conjunto_a.issubset(conjunto_c))
print(conjunto_c.issuperset(conjunto_a))

conjunto_d = {6, 7, 8, 9, 10}

print(conjunto_a.isdisjoint(conjunto_d))

conjunto_a.add(3)
conjunto_a.discard(1)
print(conjunto_a)

print(conjunto_d.pop())

print(conjunto_a.remove(2))

print(conjunto_a)

conjunto_a.clear()

print(len(conjunto_a))

print(2 in conjunto_b)
