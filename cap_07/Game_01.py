import random
from os import system, name

# Função para limpar a tela a cada execução
def limpar_tela():
    # windows
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# Função
def game():
    limpar_tela()
    print('\nBem-vindo(a) ao jogo!')
    print('Adivinhe a palavra abaixo:\n')
    # Lista de palavras para ojogo
    palavras = ['abacaxi', 'banana', 'carambola', 'vinagre', 'centurião', 'cenoura', 'relogio', 'sanduiche', 'haburgue']
    palavra = random.choice(palavras)
    letras_descobertas = ['_' for letra in palavra]
    chances = 6
    letras_errados = []

    # Logo enquanto número de chances for maior do que zero
    while chances > 0:
        print(' '.join(letras_descobertas))
        print(f'\nChances restantes {chances}')
        print(f'Letras erradas: ', " ".join(letras_errados))
        # Tentativas
        tentativa = str(input('\nDigite uma letra: ').lower())
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_errados.append(tentativa)

        if '_' not in letras_descobertas:
            print(f'\nVocê venceu, a palavra era: {palavra}')
            break

    if '_' in letras_descobertas:
        print(f'Você perdeu, a palavra era: {palavra}')


game()


