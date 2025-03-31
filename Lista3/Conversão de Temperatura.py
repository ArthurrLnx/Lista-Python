print("Conversor de Temperatura")
print("Escalas disponíveis: Celsius (C), Fahrenheit (F), Kelvin (K)")

origem = input("Escala de origem (C/F/K): ").upper()
destino = input("Escala de destino (C/F/K): ").upper()
temperatura = float(input("Digite a temperatura: "))

# Primeiro converter para Celsius se necessário
if origem == "C":
    celsius = temperatura
elif origem == "F":
    celsius = (temperatura - 32) * 5/9
elif origem == "K":
    celsius = temperatura - 273.15
else:
    print("Escala de origem inválida!")
    exit()

# Agora converter de Celsius para a escala de destino
if destino == "C":
    resultado = celsius
elif destino == "F":
    resultado = celsius * 9/5 + 32
elif destino == "K":
    resultado = celsius + 273.15
else:
    print("Escala de destino inválida!")
    exit()

print(f"{temperatura}°{origem} = {resultado:.2f}°{destino}")