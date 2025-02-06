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

print(fetch_word())
