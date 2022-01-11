def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    palavra_secreta = "banana"

    # Implementando a lista de letras acertadas.
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    # Mostrando o tamanho da palavra no início do jogo.
    print(letras_acertadas)

    while not enforcou and not acertou:

        chute = input("Qual a letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                # Implementando a substituição na lista do caracter pela letra acertada.
                letras_acertadas[index] = letra
            index = index + 1
        print(letras_acertadas)

    print("Fim do jogo.")

if __name__ == "__main__":
    jogar()
