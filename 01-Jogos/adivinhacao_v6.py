print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):

    print(f"Tentativa {rodada} de {total_de_tentativas}")

    chute = int(input("Digite um número entre 1 e 100: "))
    # Limitando as possibilidades de entrada para tratar erros.

    print("Você digitou: ", chute)

    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100!")
        continue
        # Implementando o CONTINUE para pula para a próxima iteração.
        # O mesmo poderia ter sido implamentado no WHILE.

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertou!")
        break
        # Implementando o BREAK para encerrar o laço de repetição em caso de acerto.
        # O mesmo poderia ter sido implamentado no WHILE.
    else:
        if maior:
            print("Você errou. Seu número foi MAIOR do que o número secreto.")
        elif menor:
            print("Você errou. Seu número foi MENOR do que o número secreto.")

print("Fim de jogo!")
