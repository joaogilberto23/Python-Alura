print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    # Implementando o FOR.
    # No RANGE do FOR, o último número da sequência não entra na iteração, por isso,
    # acrescenta-se em alguns casos, "+1".

    print(f"Tentativa {rodada} de {total_de_tentativas}")

    chute = int(input("Digite seu número: "))

    print("Você digitou: ", chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertou!")
    else:
        if maior:
            print("Você errou. Seu número foi MAIOR do que o número secreto.")
        elif menor:
            print("Você errou. Seu número foi MENOR do que o número secreto.")

print("Fim de jogo!")
