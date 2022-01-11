def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    # Implementando a lógica do laço de repetição no jogo.
    while not enforcou and not acertou:

        chute = input("Qual a letra? ")

        index = 0
        for letra in palavra_secreta:
            if chute == letra:
                print(f"Encontrei a letra {letra} na posição {index}.")
            index = index + 1

    print("Fim do jogo!")


if __name__ == "__main__":
    jogar()
