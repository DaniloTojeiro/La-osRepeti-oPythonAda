# Número sorteado

numSorteado = 15
numEscolhido = int(input('Informe um número entre 1 e 20: '))

while numEscolhido != numSorteado:
    numEscolhido = int(input('Você errou, tente novamente: '))

print('Parabéns você acertou!')

# Contador

contador = 0

while contador < 5:
    print(contador)

    contador = contador + 1