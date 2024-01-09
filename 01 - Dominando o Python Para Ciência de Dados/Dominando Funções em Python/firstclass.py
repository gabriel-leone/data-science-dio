def somar(a,b):
    return a+b

def subtracao(a,b):
    return a-b

def exibir_resultado(a,b,funcao):
    resultado = funcao(a,b)
    print(f'O resultado de foi {resultado}')

exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtracao)

op = somar

print(op(2,40))