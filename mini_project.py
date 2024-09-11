#Rock Paper Scissors
import random
user_score = 0
bests = "yes"
def riddle():
  point = 0
  print("Solve a riddle to get the point!")
  riddles = {"What can fill a room but takes up no space?":"light","The more you take, the more you leave behind. What are they?":"footsteps","What has a head and a tail but no body?":"coin", "What has a neck but no head?":"bottle", "What has a face and two hands but no arms or legs?":"clock","I turn once, what is out will not get in. I turn again, what is in will not get out. What am I?": "key" }
  riddle_key = list(riddles.keys())
  riddle_ans = list(riddles.values())
  index = random.randint(0,6)
  ans = (input(riddle_key[index])).lower()
  if ans == riddles[riddle_key[index]]:
    print("Correct! You got the point!")
    point +=1
  else:
    print("Not quite... the answer was", riddles.value[index])

  return point

def playGame(score, best):
  print("Welcome to rock paper scissors!" )
  play =0
  score = score
  best = best
  count =0
  best = "yes"
  
  while score < 2 and count<3 and best == "yes":
    count+=1
    user = input("Enter your play:")
  
    if user == "rock":
      play = 1
    elif user == "paper":
      play = 2
    elif user == "scissors":
      play =3
    comp = random.randint(1,3)
    if comp - play == 1 or comp - play == -2:
      print("You lose!")

    elif comp - play == 0:
      print("You tied!")
      score += riddle()
    else: 
      print("You win!")
      score+=1

    if count ==1:
      best = input("Want to do best of 3?")

  bests = best
  return score

user = playGame(user_score, bests) 

if user>= 2 and bests == "yes":
  print("You won the best of 3!")
elif user== 1 and bests == "no":
  print("Alright, you won!")
else :
  print("Sorry, you lost...")