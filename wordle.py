import random
possible_words = "great, slime, apple, smart, shoot, crazy"
word = random.choice(possible_words) 
default = '\033[0m'
green = '\033[92m'
yellow = '\033[33m'

def generate_hint(user_guess):
    color = default
    hint = ""
    for i in range(5):
        if (user_guess[i] ==word[i]):
            color = green
        elif(user_guess[i] in word):
            color= yellow
        else:
            color = default
        hint = hint + color +user_guess[i]+ default
    return hint


def game_loop():
    for i in range(6):
        guess = input("What is your guess?")
        print(generate_hint(guess))
        if guess == word:
            print("Congratulations!!!")
            break

game_loop()