# Mostra uma mensagem inicial
print("Cálculo de Juros Simples")
# Pede o valor do capital (dinheiro inicial)
capital = float(input("Digite o valor do capital (R$): "))
# Pede a taxa de juros (em porcentagem)
taxa = float(input("Digite a taxa de juros (%): "))
# Pede o tempo (em meses e anos.)
tempo = float(input("Digite o tempo: "))
# Converte a taxa de porcentagem para decimal
taxa_decimal = taxa / 100
# Calcula o valor dos juros simples (J = C * i * t)
juros = capital * taxa_decimal * tempo
# Calcula o montante final (M = C + J)
montante = capital + juros
# Mostra o valor dos juros
print("Juros:", juros)
# Mostra o montante final
print("Montante final:", montante)
