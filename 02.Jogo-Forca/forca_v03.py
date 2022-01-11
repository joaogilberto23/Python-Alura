def jogar():
    # Implemantando a função para jogar o Forca.
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    #Implementando a lógica do laço de repetição no jogo.
    while not enforcou and not acertou:

        chute = input("Qual a letra? ")
        # Implementando a função de remover espaços vazios.
        chute = chute.strip()
        index = 0
        for letra in palavra_secreta:
            # Implementando a função para deixar as letras todas maiúsculas; outra opção seria o .lower() para deixar minúsculas.
            if chute.upper() == letra.upper():
                print(f"Encontrei a letra {letra} na posição {index}.")
            index = index + 1

    print("Fim do jogo!")


if __name__ == "__main__":
    # Implantando
    jogar()
