import random

random_number = random.randint(1,10) # generates numbers 1 - 10
guess = None

while guess != random_number:
	guess = input("Guess what the random number is between 1 - 10: ")
	guess = int(guess)
	if guess < random_number:
		print("Too Low!!")
	elif guess > random_number:
	    print("Too High")
else:
	print("You have hit the mark!!")

print(random_number)

# handles user guesses
#   if they guess correct, tell them that they won
#   otherwise tell them if they are too high or too low

# BONUS - let the ployer play again if they want