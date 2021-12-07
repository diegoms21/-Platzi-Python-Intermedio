import os
import random

def read_data():
    word_list = []
    with open("./archivos/data.txt", 'r', encoding='utf-8') as f:
        for line in f:
            word_list.append(line.strip())
    #print(word_list)
    return word_list

def choose_random_word(word_list):
    word = random.choice(word_list)
    return word

def initialize_game():
    #global word_game, word_list_game
    word_list_game = read_data()
    word_game = choose_random_word(word_list_game)
    #print(word)
    print("Adivina la palabra!")
    for letter in range(len(word_game)):
        print("_", end=" ")
    print(" ")
    return word_game, word_list_game

def core_game(word_game):
    try:
        entry_letter = input("Ingresa una letra: ")
        os.system("clear")
        print("Adivina la palabra!")
        for letter in word_game:
            if entry_letter == letter:
                print(entry_letter, end=" ")
            else:
                print("_", end=" ")
        print(" ")
    except:
        pass

if __name__ == '__main__':
    word_game,word_list_game = initialize_game()
    core_game(word_game)