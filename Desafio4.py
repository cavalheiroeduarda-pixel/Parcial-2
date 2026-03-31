# Mostra as opções para o usuário
print("Calculadora Simples")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
# Pede que o usuário escolha uma operação
opcao = input("Escolha a operação (1/2/3/4): ")
# Pede o primeiro número e converte para float (permite números decimais)
num1 = float(input("Digite o primeiro número: "))
# Pede o segundo número e converte para float
num2 = float(input("Digite o segundo número: "))
# Verifica qual operação foi escolhida
if opcao == "1":
    # Calcula a soma
    resultado = num1 + num2
    # Mostra o resultado
    print("Resultado:", resultado)
elif opcao == "2":
    # Calcula a subtração
    resultado = num1 - num2
    # Mostra o resultado
    print("Resultado:", resultado)
elif opcao == "3":
    # Calcula a multiplicação
    resultado = num1 * num2
    # Mostra o resultado
    print("Resultado:", resultado)
elif opcao == "4":
    # Verifica se o segundo número é diferente de zero
    if num2 != 0:
        # Calcula a divisão
        resultado = num1 / num2
        # Mostra o resultado
        print("Resultado:", resultado)
    else:
        # Mostra erro caso tente dividir por zero
        print("Erro: divisão por zero!")
else:
    # Caso o usuário digite uma opção inválida
    print("Opção inválida!")
