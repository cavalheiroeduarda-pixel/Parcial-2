# Cria uma lista vazia para armazenar os nomes
nomes = []
# Pede 5 nomes para o usuário e adiciona na lista
print("Digite 5 nomes:")
for i in range(5):
    nome = input(f"Digite o nome {i+1}: ")  # Pede cada nome individualmente
    nomes.append(nome)  # Adiciona o nome digitado na lista
    # Imprime cada nome da lista com numeração
print("\nLista de nomes digitados:")
for i, nome in enumerate(nomes, 1): 
    # enumerate adiciona numeração automática
    print(f"{i}. {nome}")
