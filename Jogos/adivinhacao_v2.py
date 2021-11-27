print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

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

print("Fim de jogo!")
