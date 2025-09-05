import os

secret_word = 'teacher'
correct_letters = ''
attempts = 0

while True:
    letter = input('Digite uma letra: ').lower()

    if len(letter) > 1:
        print('Apenas uma letra.')
        continue

    if not letter.isalpha():
        print('Digite apenas letras.')
        continue

    if letter in correct_letters:
        print('Você já digitou essa letra.')

    attempts += 1

    if letter in secret_word:
        correct_letters += letter

    word_formed = ''
    for letter_secret in secret_word:
        if letter_secret in correct_letters:
            word_formed += letter_secret
        else:
            word_formed += '*'

    os.system('cls')
    print(word_formed)

    if word_formed == secret_word:
        print('Parabéns você acertou!')
        print(f'A palavra era {word_formed}')
        print(f'Número de tentativas {attempts}')
        to_go_out = input('Digite [s] para sair: ')
        if to_go_out == 's':
            break

