import random

numero_secreto = random.randint(1, 100)
tentativas = 0

print("Jogo de Adivinhação - Tente adivinhar o número entre 1 e 100")

while True:
    tentativa = int(input("Digite seu palpite: "))
    tentativas += 1
    
    if tentativa < numero_secreto:
        print("Muito baixo! Tente novamente.")
    elif tentativa > numero_secreto:
        print("Muito alto! Tente novamente.")
    else:
        print(f"Parabéns! Você acertou em {tentativas} tentativas!")
        break