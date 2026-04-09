#making a game of stone,paper,scissors game

import random
print("welcome to stone paper scissors game")

choices =["stone","paper","scissors"]

user = input("Enter stone,paper or scissors:").lower()
computer=random.choice(choices)

print("computer:",computer)

#tiecase
if user == computer :
    print("it's tie")

#your winning cases
elif user == "stone" and computer =="scissors":
    print("you win") 

elif user == "paper" and computer =="stone":
    print("you win")
    
elif user == "scissors" and computer =="paper":
    print("you win")


#computer winning cases
elif computer == "stone" and user == "scissors":
    print("computer wins")

elif computer == "paper" and user=="stone":
    print("computer wins")

elif computer =="scissors" and user == "paper":
    print("computer wins")

else:
    print("invalid ... try again")
    




