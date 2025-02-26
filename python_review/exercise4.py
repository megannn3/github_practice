import random
import time

def generate():
    spaces = []
    for i in range(18):
        spaces.append("red")
        spaces.append("black")
        if i==1 or i==2:
            spaces.append("green")
    return spaces


def spin_wheel(spaces):
    return random.choice(spaces)

def play_game(dollars):

    money = dollars
    bets = input("You currently have $"+str(money)+". How much do you want to bet?\n")
    if bets == "all in":
        bet = money
    else:
        bet = bets
        
    color = input("Which color are you betting on?\n")
    spaces = generate()
    landed = spin_wheel(spaces)
    print("Spinning the wheel...")
    time.sleep(2)
    if landed == color:
        money = money+ int(bet)
        print("You won! You now have $"+str(money))
    else:
        money = money - int(bet)
        print("You lost. It was "+landed+". You now have $"+str(money))
    again = input("Want to try again?\n")
    if again == "yes":
        play_game(money)


play_game(1000000000000000)
