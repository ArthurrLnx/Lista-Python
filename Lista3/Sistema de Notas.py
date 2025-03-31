nota = float(input("Digite a nota do aluno (0-100): "))

if 90 <= nota <= 100:
    conceito = "A"
elif 80 <= nota < 90:
    conceito = "B"
elif 70 <= nota < 80:
    conceito = "C"
elif 60 <= nota < 70:
    conceito = "D"
else:
    conceito = "F"

print(f"Conceito: {conceito}")