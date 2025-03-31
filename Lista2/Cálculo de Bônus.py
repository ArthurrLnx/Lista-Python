salario = float(input("Digite seu salário: "))
tempo_servico = int(input("Digite seu tempo de serviço (em anos): "))

if tempo_servico > 5:
    bonus = salario * 0.10
else:
    bonus = salario * 0.05

print(f"Seu bônus será de: R$ {bonus:.2f}")