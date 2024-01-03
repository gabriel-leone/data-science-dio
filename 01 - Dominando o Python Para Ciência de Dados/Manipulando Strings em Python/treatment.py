palavra = "   palavra  "
print(palavra.strip()) # Remove espaços em branco
print(palavra.rstrip()) # Remove espaços em branco à direita
print(palavra.lstrip()) # Remove espaços em branco à esquerda

python = "Python"
print(python.center(20, "$")) # Centraliza a string
print(".".join(python)) # Adiciona um caractere entre cada letra
print(python.replace("P", "J")) # Substitui caracteres