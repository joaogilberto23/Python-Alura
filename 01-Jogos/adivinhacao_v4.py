print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while rodada <= total_de_tentativas:

    print(f"Tentativa {rodada} de {total_de_tentativas}")

    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    # Implementando as duas formas de utilizar o método FORMAT.

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

    rodada = rodada + 1

print("Fim de jogo!")
