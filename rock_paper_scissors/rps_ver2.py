from random import randint
print("Rock...")
print("Paper....")
print("Scissors....\n")

player = input("Player, make your move: ").lower()

rand_num = randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print(f"Computer plays {computer}\n")

if player == computer:
    print("It's a tie!!")

elif player == "rock":
    if computer == "scissors":
        print("player wins!!")
    else:
        print("Computer wins!!")

elif player == "paper":
    if computer == "rock":
        print("Player wins!!")
    else:
        print("Computer wins!!")

elif player == "scissors":
    if computer == "paper":
        print("Player wins!!")
    else:
        print("Computer wins!!")
else:
    print("Please enter a valid move")