import forca
import adivinhacao


def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu Jogo!*******")
    print("*********************************")

    print("\n(1) Forca"
          "\n(2) Adivinhação")
    # Implementando menu de seleção de jogos.

    jogo = int(input("\nQual o jogo? "))

    if jogo == 1:
        print("Jogando forca")
        forca.jogar()
        # Implementando função de chamada do jogo da Forca.
    elif jogo == 2:
        print("Jogando adivinhação")
        adivinhacao.jogar()
        # Implementando função de chamada do jogo de Adivinhação.


if __name__ == "__main__":
    escolhe_jogo()

    """Quando rodamos diretamente um arquivo no Python, ele internamente cria uma variável e a preenche.
    Através dessa variável podemos fazer uma consulta, pois se ela estiver preenchida,
    significa que o arquivo foi executado diretamente, mas se a variável não estiver preenchida,
    então significa que o arquivo só foi importado. Essa variável é a __name__,
    e ela é preenchida com o valor __main__ caso o arquivo seja executado diretamente. """
