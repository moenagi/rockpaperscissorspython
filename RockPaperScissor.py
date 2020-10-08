import random
mylist = ['paper','rock','scissor']
mylist1 =(random.choice(mylist))
print(mylist1)

username = input("Enter username:")
while mylist1 == ("paper"):
    if username == "rock":
        print("you lost")
        break
    if username == "scissor":
        print("You win")
        break
    else:
       print("Its  Tie")
       break
while mylist1 == ("rock"):
    if username == "paper":
        print("you win")
        break
    if username == "scissor":
        print("You lost")
        break
    else:
        print("Its  Tie")
        break
        
while mylist1 == ("scissor"):
    if username == "rock":
        print("you win")
        break
    if username == "paper":
        print("You lost")
        break
    else:
        print("Its  Tie")
        break






 


