def calcular_total(numeros):
  return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
  antecessor = numero - 1
  sucessor = numero + 1

  return antecessor, sucessor

def none():
  print(' ')

print(calcular_total([10,20,30,40]))
print(retorna_antecessor_e_sucessor(10))
print(none())