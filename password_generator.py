import random
import string
import requests

def random_character():
    choices = string.ascii_letters + string.digits + string.punctuation
    return random.choice(choices)




def generate_strong_password():
    password_length = int(input("How long do you want your password to be? Enter a number."))        
    password = ""
    for i in range(password_length):
        password = password + random_character()
    print(password)

generate_strong_password()

def fetch_word():
    url = "https://random-word-api.herokuapp.com/word?length=15"
    response  = requests.get(url)
    word = response.json()[0]
    return word

def replace_letters(word):
    word =word[0].upper()+word[1:]
    if "a" in word:
        word = word.replace("a","@")
    if "i" in word:
        word = word.replace("i","j")
    if "b" in word:
        word = word.replace("b","&")
    if "l" in word:
        word = word.replace("l","#")
    if "k" in word:
        word = word.replace("k","%")
    return word

def generate_password():
    password = replace_letters(fetch_word())+replace_letters(fetch_word())
    print(password)


generate_password()


