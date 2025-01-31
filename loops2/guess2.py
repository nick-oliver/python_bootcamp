import random

random_number = random.randint(1,10) # generates numbers 1 - 10
# guess = None

while True:
	guess = input("Guess what the random number is between 1 - 10: ")
	guess = int(guess)
	if guess < random_number:
		print("Too Low!!")
	elif guess > random_number:
	    print("Too High")
	else:
		print("You have hit the mark!!")
		play_again = input("Do you want to play again? y/n ")
		if play_again == "y":
			random_number = random.randint(1,10) # generates numbers 1 - 10
			guess = None
		else:
			print("Thanks for playing. Come again!")
			break

# print(random_number)

