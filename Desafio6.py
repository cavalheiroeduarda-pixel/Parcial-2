  # Mostra o menu para o usuário
print("Conversor de Tempo")
print("1 - Converter segundos para h/m/s")
print("2 - Converter h/m/s para segundos")
  # Pede qual a opção do usuário
opcao = input("Escolha uma opção (1 ou 2): ")
  # Se a opção for 1: segundos → horas/minutos/segundos
if opcao == "1":
  # Pede o total de segundos
    total_segundos = int(input("Digite o tempo em segundos: "))
  # Calcula as horas (1 hora = 3600 segundos)
    horas = total_segundos // 3600
  # Calcula o restante dos segundos
    resto = total_segundos % 3600
  # Calcula os minutos (1 minuto = 60 segundos)
    minutos = resto // 60
  # Calcula os segundos restantes
    segundos = resto % 60
  # Mostra o resultado
    print("Tempo:", horas, "h", minutos, "min", segundos, "s")
  # Se a opção for 2: horas/minutos/segundos → segundos
elif opcao == "2":
  # Pede as horas
    horas = int(input("Digite as horas: "))
  # Pede os minutos
    minutos = int(input("Digite os minutos: "))
  # Pede os segundos
    segundos = int(input("Digite os segundos: "))
  # Converte tudo para segundos
    total_segundos = (horas * 3600) + (minutos * 60) + segundos
  # Mostra o resultado
    print("Total em segundos:", total_segundos)
  # Caso a opção seja inválida
else:
    print("Opção inválida!")
