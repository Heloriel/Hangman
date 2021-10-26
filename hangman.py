import random
import words_list as wl
import re
import sys


lifes = 6
used_letters = []


def game_over():
    print("")
    print("\033[91m Suas vidas se esgotaram! x.x Game Over! ")
    print("")
    sys.exit()


def input_check():
    letter = input("Escolha uma letra: ")
    if not re.match("^[a-z]*$", letter):
        print("Entrada inválida! Tente novamente.")
        print("\n")
        return False
    elif letter == "exit":
        print("Encerrando...")
        sys.exit()
    elif letter == "list":
        print(f"Letras usadas: {used_letters}")
        return False
    elif len(letter) > 1 or len(letter) <= 0:
        print("Entrada inválida! Tente novamente.")
        print("\n")
        return False
    elif letter in used_letters:
        print(f"Você já utilizou a letra '{letter.upper()}'! Tente novamente.")
        return False
    else:
        used_letters.append(letter.upper())
        return letter.upper()


def hangman_game(hangman, word, lifes_remaining):
    print(f"Você tem {lifes_remaining} vidas restantes!")
    if lifes_remaining <= 0:
        game_over()
    for x in hangman:
        print(x, end=" ")
    print("\n")
    letter = input_check()
    if not letter:
        hangman_game(hangman, word, lifes_remaining)
    else:
        for index, val in enumerate(word):
            if letter not in word:
                print(f"Desuclpe, mas a palavra não possui a letra '{letter.upper()}'.")
                lifes_remaining -= 1
                break
            else:
                if letter == val:
                    hangman[index] = letter
        if "-" not in hangman:
            for x in hangman:
                print(x, end=" ")
            print("\n")
            print("\033[92m yaaaayyyyy!!!! You win!")
            print("\n")
        else:
            hangman_game(hangman, word, lifes_remaining)


def start():
    selected_word = random.randint(0, (wl.words.__len__() - 1))
    word = wl.words[selected_word].upper()
    hangman = []
    for _ in word:
        hangman.append("-")

    hangman_game(hangman, word, lifes)


start()
