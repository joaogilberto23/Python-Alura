print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while rodada <= total_de_tentativas:
    print(f"Tentativa {rodada} de {total_de_tentativas}")
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    # Acima, as duas formas de utilizar o método FORMAT.
    chute = int(input("Digite seu número: "))
    # A função input sempre registra o valor informado como string a partir do Python 3, por isso,
    # é preciso especificar o tipo se for fazer algum tipo de compatação entre variáveis.

    print("Você digitou: ", chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertou!")
    else:
    # ELSE em Python não aceita receber condição, para isso, usa-se ELIF.
        if maior:
            print("Você errou. Seu número foi MAIOR do que o número secreto.")
        elif menor:
            print("Você errou. Seu número foi MENOR do que o número secreto.")

    rodada = rodada + 1

print("Fim de jogo!")
