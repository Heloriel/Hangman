import random
import words_list as list
import re
import sys

def InputCheck():
    letter = input("Escolha uma letra: ")
    if not re.match("^[a-z]*$", letter):
        print("Entrada inválida! Tente novamente.")
        print("\n")
    elif len(letter) > 1 or len(letter) <= 0:
        print("Entrada inválida! Tente novamente.")
        print("\n")
    else:
        return letter.upper()

def Hangman(hangman, result):
    for x in hangman:
        print(x, end=" ")
    print("\n")
    letter = InputCheck()
    for index, val in enumerate(result):
        if letter == val:
            hangman[index] = letter;
    if not "-" in hangman:
        for x in hangman:
            print(x, end=" ")
        print("\n")
        print("yaaaayyyyy!!!! You win!")
        print("\n")
    else:
        Hangman(hangman, result)
                    

def Start():
    selected_word = random.randint(0, (list.words.__len__() - 1))
    word = list.words[selected_word].upper()
    result = []
    hangman = []
    for x in word:
        result.append(x)
    for letter in result:
        hangman.append("-")
    Hangman(hangman, result)
    
Start()


#print(hangman)

#print(word)

