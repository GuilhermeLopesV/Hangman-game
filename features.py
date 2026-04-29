import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def game(secret_word, tip, correct_letters, attempts):
    while True:
        clear()

        word_formed = ''.join(
            letter if letter in correct_letters else '*'
            for letter in secret_word
        )
        print(f'Palavra: {word_formed}')
        print(f'Dica: {tip}')
        print(f'Tentativas: {attempts}')
        print(f'Letras usadas: {" ".join(sorted(correct_letters))}\n')

        letter = input('Digite uma letra: ').lower().strip()

        if len(letter) != 1:
            print('⚠️ Digite apenas uma letra.')
            input('Pressione ENTER para continuar...')
            continue

        if not letter.isalpha():
            print('⚠️ Apenas letras são permitidas.')
            input('Pressione ENTER para continuar...')
            continue

        if letter in correct_letters:
            print('⚠️ Você já tentou essa letra.')
            input('Pressione ENTER para continuar...')
            continue

        attempts += 1
        correct_letters.add(letter)

        if all(l in correct_letters for l in secret_word):
            clear()
            print(f'🎉 Parabéns! Você acertou: {secret_word}')
            print(f'Número de tentativas: {attempts}')
            break