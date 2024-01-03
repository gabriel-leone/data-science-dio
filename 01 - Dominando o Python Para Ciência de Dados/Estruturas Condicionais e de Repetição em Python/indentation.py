def sacar(self, valor: float) -> None:
  if self.saldo < valor:
    print("Saldo insuficiente.")
  else:
    self.saldo -= valor
    print("Saque realizado com sucesso.")