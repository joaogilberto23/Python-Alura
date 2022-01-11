def jogar():
    # Implemantando a função para jogar o Forca.
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

    #Implementando a lógica do laço de repetição no jogo.
    while not enforcou and not acertou:

        chute = input("Qual a letra? ")
        # Implementando a função de remover espaços vazios.
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            # Implementando a função para deixar as letras todas maiúsculas; outra opção seria o .lower() para deixar minúsculas.
            if chute.upper() == letra.upper():
                # Implementando a substituição na lista do caracter pela letra acertada.
                letras_acertadas[index] = letra
            index = index + 1
        print(letras_acertadas)


if __name__ == "__main__":
    # Implantando
    jogar()
