# Solicita que o usuário que insira um número
numero = input("Digite um número: ")
# Converte a entrada do usuário de string para inteiro
numero = int(numero)
# Verifica se o número é par
if numero % 2 == 0:
  # Se o número for par, imprime uma mensagem correspondente
    print(numero, "é um número par.")
else:
  # Se o número não for par, imprime uma mensagem correspondente
    print(numero, "não é um número par.")
