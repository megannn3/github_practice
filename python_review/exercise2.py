import random


random_num = random.randint(0,100)
a= True
guesses =0
while a == True:
    guess = int(input("Guess a random number \n"))
    guesses += 1


    if guess < random_num:
        print("You guessed too low")
    elif guess> random_num:
        print("You guessed too high")
    elif guess == random_num:
        print("you guessed correctly!")
        print(guesses)
        a=False