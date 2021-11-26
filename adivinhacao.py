print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute = int(input("Digite seu número: "))
# A função input sempre registra o valor informado como string a partir do Python 3, por isso,
# é preciso especificar o tipo se for fazer algum tipo de compatação entre variáveis.

print("Você digitou: ", chute)

if chute == numero_secreto:
    print("Você acertou!")
else:
    print("Você errou.")
