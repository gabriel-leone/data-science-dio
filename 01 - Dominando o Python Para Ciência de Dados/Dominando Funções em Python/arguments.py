def salvar_carro(marca, modelo, ano, placa):
    # Salva no banco de dados
    print(f"Carro inserido com sucesso: {marca} / {modelo} / {ano} / {placa}")

salvar_carro("Ford", "Ka", "2021", "ABC1234")
salvar_carro(marca="Ford", modelo="Ka", ano=2021, placa="ABC1234")
salvar_carro(**({"marca": "Ford", "modelo": "Ka", "ano": 2021, "placa": "ABC1234"}))

print("\n")

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Segunda-feira, 8 de janeiro de 2024","Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC1234", marca="Fiat", motor="Fire", combustivel="Flex")
# A linha abaixo dá erro
# criar_carro(modelo="Palio", "ano"=1999, "placa" = "ABC1234", marca="Fiat", motor="Fire", combustivel="Flex")
criar_carro("Palio", 1999, "ABC1234", "Fiat", "Fire", "Flex")

def remover_carro(*, modelo, ano, placa):
    print(modelo, ano, placa)

# A linha abaixo dá erro porque o * significa Keyword only
# criar_carro("Palio", 1999, "ABC1234")
remover_carro(modelo="Palio", ano="1999", placa="ABC1234")

def quebrar_carro(modelo, marca, ano, /, *, placa, motor, combustivel):
    print(modelo, marca, ano, placa, motor, combustivel)

quebrar_carro("Palio", "Fiat", 1999, placa="ABC1234", motor="Fire", combustivel="Flex")