print("Calculadora Simples")
print("Operações disponíveis:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Escolha uma operação (1-4): "))
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == 1:
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")
elif opcao == 2:
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")
elif opcao == 3:
    resultado = num1 * num2
    print(f"Resultado: {num1} * {num2} = {resultado}")
elif opcao == 4:
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado}")
    else:
        print("Erro: Divisão por zero!")
else:
    print("Opção inválida!")