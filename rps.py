from random import randint

rps = ["Rock", "Paper", "Scissors"]

computer = rps[randint(0,2)]
player = False
while player == False:
    player = input("Rock, Paper, Scissors?")
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
player=False
computer=rps[randint(0,2)]








# if comp == r and y == s:
#     print("You win")
#     elif x = r and y = p:
#         print("You lose")
#         elif x = s and y = p:
#             print("You win")
#             elif x = y:
#                 print("DRAW")
