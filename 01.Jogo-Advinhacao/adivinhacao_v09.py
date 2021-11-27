import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0

pontos = 1000
# Implementando pontuação no jogo.

print("Qual o nível de dificuldade?")
print("(1)-Fácil (2)-Médio (3)-Difícil")

nivel = int(input("Defina o nível: "))
if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):

    print(f"Tentativa {rodada} de {total_de_tentativas}")

    chute = int(input("Digite um número entre 1 e 100: "))

    print("Você digitou: ", chute)

    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print(f"Você acertou e fez {pontos} pontos!")
        # Implementando a informação da pontuação ao conseguir finalizar o jogo.
        break
    else:
        if maior:
            print("Você errou. Seu número foi MAIOR do que o número secreto.")
        elif menor:
            print("Você errou. Seu número foi MENOR do que o número secreto.")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
        # Implementando pontuação no jogo.
        # O jogador será descontado a cada chute errado.
        # Para os lógica dos pontos perdidos não gerar um número negativo, utilizamos a função ABS().

print("Fim de jogo!")
