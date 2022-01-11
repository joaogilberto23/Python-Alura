def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    # Usando a função para deixar a palavra secreta em letras maiúsculas.
    palavra_secreta = "banana".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    # Implementando a lógica das tentativas.
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:

        chute = input("Qual a letra? ")
        # Usando a função para deixar o chute também em letras maiúsculas após a remoção dos espaços vazios.
        chute = chute.strip().upper()

        # Verificando se o chute está contido na palavra secreta.
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute.upper() == letra.upper():
                    letras_acertadas[index] = letra
                index += 1  # Formatando o incremento de forma mais enxuta.
        else:
            erros += 1
            # Informando o restante de tentativas.
            print(f"Ops, você errou! Faltam {6 - erros} tentativas.")

        # Implementando o máximo de tentativas.
        enforcou = erros == 6

        # Implementando a finalização do jogo quando a palavra for completada.
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    # Implementando mensagens de término do jogo.
    if acertou:
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    print("Fim do jogo.")


if __name__ == "__main__":
    jogar()
