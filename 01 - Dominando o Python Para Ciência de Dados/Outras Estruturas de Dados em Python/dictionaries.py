pessoa1 = {"nome": "Gabriel Leone", "idade": 19}

pessoa2 = dict(nome="Gabriel Leone", idade=19)

pessoa1["telefone"] = "11999999999"

print(pessoa1)
print(pessoa2)
print(pessoa1["nome"])

for chave in pessoa1:
    print(chave, pessoa1[chave])
    
### METODOS

# clear, copy, pop, popitem,

dict.fromkeys(["nome", "telefone"])

print(pessoa1.get("nome"))

novo_dicionario = {"a": 100, 1: "teste", "b": "python"}
print(novo_dicionario.keys())

contato = {"nome": "Gabriel Leone", "telefone": "119999999999"}

contato.setdefault("nome", "Maria Clara")
print(contato)

contato.setdefault("idade", 19)
print(contato)

contato.update({"nome": "Gabriel Leone"})
print(contato)

contato.update({"nome": "Gabriel Leone", "telefone": "119999999999", "idade": 19, "cep": "2918457125"})
print(contato)

print(contato.values())