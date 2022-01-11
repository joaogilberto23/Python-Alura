import random  # Importando a biblioteca para usar a função aleatória.


def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    # Implementando leitura de arquivo.

    arquivo = open("palavras.txt", "r")  # Abrindo o arquivo txt com as palavras que serão utilizadas no jogo.

    palavras = []

    for linha in arquivo:  # Percorrendo o arquivo linha a linha.
        linha = linha.strip()  # Removendo a quebra de linha.
        palavras.append(linha)  # Adicionando cada palavra tratada na lista "palavras".

    arquivo.close()  # Fechando o arquivo lido.

    numero = random.randrange(0, len(palavras))  # Implementando a escolha de um número de index aleatório dentro do range de palavras.
    palavra_secreta = palavras[numero].upper()  # Escolhendo a palavra através do index aleatório acima.

    letras_acertadas = ["_" for letra in palavra_secreta]
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

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


if __name__ == "__main__":
    jogar()
