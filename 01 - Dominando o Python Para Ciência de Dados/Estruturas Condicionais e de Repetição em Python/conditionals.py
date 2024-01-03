SALDO_USUARIO = 2000.0

opcao = int(input("Informe a opção desejada:\n[1] Sacar\n[2] Extrato\n"))

if opcao == 1:
  saque = float(input("Digite o valor do saque: "))
  if saldo >= saque:
    print("Saque realizado com sucesso.")
  else:
    print("Saldo insuficiente.")
elif opcao == 2:
  print("Mostrando extrato......")
else:
  print("Opção inválida.")

status = "Sucesso" if SALDO_USUARIO >= 0 else "Falha"
print(f"Status da operação: {status}")