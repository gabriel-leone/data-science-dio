menu = """

[d] - Depositar
[s] - Sacar
[e] - Extrato
[s] - Sair

"""

saldo = 1000.0
limite = 500.0
numero_saques = 0
LIMITE_SAQUES = 3
user_input = ""

def deposito(valor_depositado):
  global saldo

  saldo += valor_depositado
  print(f"Depósito de R$ {valor_depositado} realizado com sucesso.\n")

def saque(valor_saque):
  global saldo
  global extrato
  global numero_saques

  if numero_saques >= LIMITE_SAQUES:
    print("Limite de saques diários atingido.")
    return

  if saldo < valor_saque:
    print("Saldo insuficiente.")
    return

  saldo -= valor_saque
  print(f"Saque de R$ {valor_saque} realizado com sucesso.\n")
  numero_saques += 1

def tirar_extrato():
  global extrato
  global saldo
  global limite

  print(f"""
##################################################################
#                       Bem vindo ao banco!                      #
# Seu saldo atual é de R$ {saldo} e seu limite é de R$ {limite}. #
##################################################################


""")


while user_input != "q":
  print(menu)
  opcao = input("Digite a opção desejada: ")

  if opcao == "d":
    valor_depositado = float(input("Digite o valor do depósito: "))
    deposito(valor_depositado)
  elif opcao == "s":
    valor_saque = float(input("Digite o valor do saque: "))
    saque(valor_saque)
  elif opcao == "e":
    tirar_extrato()
  elif opcao == "q":
    print("Saindo do programa...")
    break