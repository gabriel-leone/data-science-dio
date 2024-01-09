texto_menu = """

[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair

"""

def depositar(saldo, valor):
    saldo += valor
    return saldo

def sacar(saldo, valor):
    saldo -= valor
    return saldo

def extrato(saldo):
    print(f'Saldo: {saldo:.2f}')

def mensagem_sucesso(saldo):
    print(saldo)
    print(f"""
    Operação realizada com sucesso!
    Saldo: R${saldo:.2f}
    """)

input_usuario = ''
saldo = 0.0

while input_usuario != 'q':
    operacao = ''

    print(texto_menu)

    input_usuario = input('Digite a opção desejada: ')

    if input_usuario == 'd':
        valor_deposito = float(input('Digite o valor: '))
        saldo = depositar(saldo, valor_deposito)
        mensagem_sucesso(saldo)
    elif input_usuario == 's':
        valor_sacado = float(input('Digite o valor: '))
        saldo = sacar(saldo, valor_sacado)
        mensagem_sucesso(saldo)
    elif input_usuario == 'e':
        extrato(saldo)
    else:
        quit()
