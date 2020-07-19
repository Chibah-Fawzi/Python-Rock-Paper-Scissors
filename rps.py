from random import randint

rps = ["Rock", "Paper", "Scissors"]

computer = rps[randint(0,2)]
player = True
while player == True:    
    player = input("Rock, Paper, Scissors?")
    print("Welcome to the rock, paper, scissors game!")
    if player == computer:
        print("Draw")
    
    elif player == "Rock":
        if computer == "Paper":
            print(f"computer used {computer} so you lose")

        else:
                print(f"computer used {computer} so you win")
    elif player == "Scissors":
        if computer == "Rock":
            print(f"computer used {computer} so you lose")
        else:
                print(f"computer used {computer} so you win")
    elif player == "Paper":
        if computer == "Scissors":
         print(f"computer used {computer} so you lose")
        else:
            print(f"computer used {computer} so you win")
    else:
        print("thats not a valid player")      
