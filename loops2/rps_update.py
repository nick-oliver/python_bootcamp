from random import randint
player_wins = 0
computer_wins = 0
winning_score = input("Player, how many wins do you want to call it a match? " )
winning_score = int(winning_score)


# for times in range(3):  #very simple

while player_wins < winning_score and computer_wins < winning_score:
    print(f"(Player score: {player_wins} Computer Score: {computer_wins})")
    print("Rock...")
    print("Paper....")
    print("Scissors....\n")

    player = input("Player, make your move: ").lower()
    if player == "quit" or player == "q":
        break
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
            print("Player wins! YAY!!")
            player_wins += 1
        else:
            print("Computer wins! BOO!!")
            computer_wins += 1

    elif player == "paper":
        if computer == "rock":
            print("Player wins! YAY!!")
            player_wins += 1
        else:
            print("Computer wins! BOO!!")
            computer_wins += 1

    elif player == "scissors":
        if computer == "paper":
            print("Player wins! YAY!!")
            player_wins += 1
        else:
            print("Computer wins! BOO!!")
            computer_wins += 1
    else:
        print("Please enter a valid move")
print(f"FINAL SCORE... Player score: {player_wins} Computer Score: {computer_wins}")

if player_wins > computer_wins:
    print ("CONGRATS! YOU WON!!")
elif player_wins == computer_wins:
    print ("It's a tie")
else:
    print ("BOO! THE COMPUTER WON!")
