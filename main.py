from features import game
from data import words
import random

while True:
    start = input('Aperte Enter para iniciar ...')

    item = random.choice(words)
    secret_word = item["word"]
    tip = item["tip"]
    correct_letters = set()
    attempts = 0

    game(secret_word, tip, correct_letters, attempts)

    to_go_out = input('Digite [s] ser quiser sair: ')
    if to_go_out == 's':
        break