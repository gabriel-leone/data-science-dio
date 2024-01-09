def exibir_mensagem():
  print('Hello world!')
  
def exibir_mensagem_2(nome):
  print(f'Hello, {nome}')
  
def exibir_mensagem_3(nome="Anonimo"):
  print(f'Hello, {nome}')
  
exibir_mensagem()
exibir_mensagem_2(nome='Gabriel')
exibir_mensagem_3()
exibir_mensagem_3(nome='Gabriel')
exibir_mensagem_2('Gabriel')