# Exemplo 1:
print("Tentativa {} de {}".format(1, 3))

# Invertendo os parâmetros através dos índices:
print("Tentativa {1} de {0}".format(1, 3))

# Indicando o tipo de dado, neste exemplo, float:
print("R$ {:f}".format(1.59))

# Limitando o número de casas decimais após o ponto:
print("R$ {:.2f}".format(1.59))

# Definindo  total de caracteres, neste caso 7, 4 antes do ponto, o ponto e duas casas após o ponto:
# Se o dado não contiver números a esquerda, serão exibidos espaços em branco.
print("R$ {:7.2f}".format(1.5))

# Preenchendo os espaços em branco com zeros:
print("R$ {:07.2f}".format(1.5))

# Formatando DATAS:
print("Data {:02d}/{:02d}".format(9, 4))
print("Data {:02d}/{:02d}".format(19, 11))

