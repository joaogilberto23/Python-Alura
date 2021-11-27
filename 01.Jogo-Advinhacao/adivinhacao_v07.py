import random
# Importando a biblioteca RANDOM para gerar números aleatórios.

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
# Implementando a função RANDOM que vai gerar um número aleatório entre 1 e 100.

total_de_tentativas = 3

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
        print("Você acertou!")
        break
    else:
        if maior:
            print("Você errou. Seu número foi MAIOR do que o número secreto.")
        elif menor:
            print("Você errou. Seu número foi MENOR do que o número secreto.")

print("Fim de jogo!")
