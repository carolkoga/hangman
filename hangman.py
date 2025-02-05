import random

palavras_pt = ['maçã', 'computador', 'elefante', 'guitarra', 'montanha', 'sussurro', 'quebra-cabeça', 'universo',
               'bicicleta', 'arco-íris', 'oceano']
palavras_en = ['apple', 'computer', 'elephant', 'guitar', 'mountain', 'whisper', 'puzzle', 'universe', 'bicycle',
               'rainbow', 'ocean']

idioma = input('Digite 1 para Portugues. Write 2 for English: ')
if idioma == '1':
    palavra_escolhida = random.choice(palavras_pt)
    print(f"A palavra escolhida em {len(palavra_escolhida)} letras.")
elif idioma == '2':
    palavra_escolhida = random.choice(palavras_en)
    print(f'The word has {len(palavras_en)} letters.')
else:
    print('Opção inválida.')

oculta = '_'*len(palavra_escolhida)
max_tentativas = 6
letras = []

while True:
    print(oculta)
    if idioma == '1':
       letra = input('Digite uma letra: ').lower()
    elif idioma == '2':
        letra = input('Write a word: ').lower()

    if letra in letras:
        if idioma == '1':
            print('Você ja digitou esta letram digite outra para continuar: ')
        elif idioma == '2':
            print('You already typed this word. Type another to continue: ')
        continue

    letras.append(letra)

    if letra in palavra_escolhida:
        lista_atual = []
        for index in range(len(palavra_escolhida)):
            if letra == palavra_escolhida[index]:
                lista_atual.append(letra)
            else:
                lista_atual.append(oculta[index])
        oculta = ''.join(lista_atual)
    else:
        max_tentativas -= 1
        if idioma == '1':
            print(f'Letra não encontrada. Você tem mais {max_tentativas} tentativas.')
        elif idioma == '2':
            print(f'Letter not found. You have {max_tentativas} more attempts.')
    if palavra_escolhida == oculta:
        if idioma == '1':
            print(f'Parabéns, você ganhou! A palavra é {palavra_escolhida}.')
        elif idioma == '2':
            print(f'Congratulations, you won! The word is {palavra_escolhida}.')
        break
    elif max_tentativas == 0:
        if idioma == '1':
            print(f'Você perdeu. A palavra sorteada era {palavra_escolhida}.')
        elif idioma == '2':
            print(f'You lost. The word was {palavra_escolhida}.')
        break