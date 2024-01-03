texto = input("Digite um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
  if letra.upper() in VOGAIS:
    print(letra.upper(), end="")
  else:
    print(letra.lower(), end="")

print()

for numero in range(10):
  print(numero, end="")

print()

for numero in range(1, 11):
  print(numero, end="")

print()

for numero in range(1, 11, 2):
  print(numero, end="")

print()

for numero in range(10, 0, -1):
  print(numero, end="")

print()

opcao = -1

while opcao != 0:
  opcao = int(input("Digite um número: [0] Para sair\n"))
  print(f"Você digitou {opcao}")
  if opcao == 0:
    print("Saindo do programa...")
    break