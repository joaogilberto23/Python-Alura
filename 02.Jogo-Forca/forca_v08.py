import random


# Enxugando o código:
def jogar():
    mensagem_abertura()  # Criando uma função para encapsular a mensagem de abertura.
    palavra_secreta = carrega_palavra_secreta()  # Criando uma função para encapsular o carregamento da palavra secreta.
    letras_acertadas = inicializa_letras_acertadas(
        palavra_secreta)  # Criando uma função para encapsular a exibição de quantas letras tem a palavra secreta.

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:

        chute = input("Qual a letra? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute.upper() == letra.upper():
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print(f"Ops, você errou! Faltam {len(palavra_secreta) - erros} tentativas.")

        enforcou = erros == len(palavra_secreta)
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if acertou:
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    print("Fim do jogo.")


def mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]


if __name__ == "__main__":
    jogar()
